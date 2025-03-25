from jinja2 import Template
import graphviz

# Define templates for Modelica components
context_template = Template(
    """
PNlib.Components.PD {{ place }}(nIn = {{ n_in }}, nOut = {{ n_out }}, maxTokens = 1);
{{ activate }}({% if activate_event is not none %}event = {{ activate_event }}{% endif %}{% if activate_event is not none and activate_condition is not none %}, {% endif %}{% if activate_condition is not none %}firingCon = {{ activate_condition }}{% endif %}{% if activate_event is not none or activate_condition is not none %}, {% endif %}nIn = {{ t_a_in }}, nOut = {{ t_a_out }});
{{ deactivate }}({% if deactivate_event is not none %}event = {{ deactivate_event }}{% endif %}{% if deactivate_event is not none and deactivate_condition is not none %}, {% endif %}{% if deactivate_condition is not none %}firingCon = {{ deactivate_condition }}{% endif %}{% if deactivate_event is not none or deactivate_condition is not none %}, {% endif %}nIn = {{ t_d_in }});
    """
)

weak_inclusion_template = Template(
    """
PNlib.Components.IA {{ inhibitor }};
{{ deactivate_duplicate }}({% if deactivate_event is not none %}event = {{ deactivate_event }}{% endif %}{% if deactivate_event is not none and deactivate_condition is not none %}, {% endif %}{% if deactivate_condition is not none %}firingCon = {{ deactivate_condition }}{% endif %}{% if deactivate_event is not none or deactivate_condition is not none %}, {% endif %}nIn = {{ duplicate_n_in }}, nOut = 0);
    """
)

strong_inclusion_template = Template(
    """
PNlib.Components.IA {{ inhibitor }};
{{ deactivate_duplicate }}({% if deactivate_event is not none %}event = {{ deactivate_event }}{% endif %}{% if deactivate_event is not none and deactivate_condition is not none %}, {% endif %}{% if deactivate_condition is not none %}firingCon = {{ deactivate_condition }}{% endif %}{% if deactivate_event is not none or deactivate_condition is not none %}, {% endif %}nIn = {{ duplicate_n_in }}, nOut = 0);
    """
)

exclusion_template = Template(
    """
PNlib.Components.IA {{ inhibitor }};
    """
)

requirement_template = Template(
     """
PNlib.Components.IA {{ inhibitor }};
{{ deactivate_duplicate }}({% if deactivate_event is not none %}event = {{ deactivate_event }}{% endif %}{% if deactivate_event is not none and deactivate_condition is not none %}, {% endif %}{% if deactivate_condition is not none %}firingCon = {{ deactivate_condition }}{% endif %}{% if deactivate_event is not none or deactivate_condition is not none %}, {% endif %}nIn = {{ duplicate_n_in }}, nOut = 0);
    """
)

equation_template = Template(
    """
equation
    {% for conn in connections %}
    connect({{ conn[0] }}, {{ conn[1] }});
    {% endfor %}
    """
)

# Context-oritend Petri Nets Compositor Class
class CoPNCompositor:
    def __init__(self, contexts, weak_inclusions, strong_inclusions, exclusions, requirements, event_definitions):
        self.contexts = contexts
        self.weak_inclusions = weak_inclusions
        self.strong_inclusions = strong_inclusions
        self.exclusions = exclusions
        self.requirements = requirements
        self.event_definitions = event_definitions

    def generate_contexts(self):
        """Generate Modelica code with accurate port counts for contexts and relations."""
        global place_ports

        # Initialize place ports for contexts and their transitions
        place_ports = {name: {"in": 0, "out": 0} for name in contexts}
        place_ports.update({f"{name}_activate": {"in": 0, "out": 0} for name in contexts})
        place_ports.update({f"{name}_deactivate": {"in": 0, "out": 0} for name in contexts})
        
        # Dictionaries to store unique names
        unique_names = {"duplicates": {}, "inhibitors": {}}
        # Track used ports
        used_ports = {"out": {}, "in": {}}
        # Store connections between components
        connections = []
        # Accumulate generated Modelica code
        modelica_code = []

        def get_unique_name(category, base_name):
            """Generate and retrieve unique names for components."""
            if base_name not in unique_names[category]:
                unique_names[category][base_name] = f"{base_name}_1"
            return unique_names[category][base_name]
        
        def get_next_port(component, port_type):
            """Allocate the next available port for a component."""
            if component not in used_ports[port_type]:
                used_ports[port_type][component] = 1
            else:
                used_ports[port_type][component] += 1

            # Update the nIn/nOut count for the component
            if component in place_ports:
                place_ports[component][port_type] += 1
            return used_ports[port_type][component]

        # Generate connections for contexts
        for context in self.contexts:
            activate = f"{context}_activate"
            deactivate = f"{context}_deactivate"
            events = self.event_definitions[context]

            activation_time = events.get("activation_time", None)
            activation_condition = events.get("activation_condition", None)
            deactivation_time = events.get("deactivation_time", None)
            deactivation_condition = events.get("deactivation_condition", None)

            connections.append((f"{activate}.outPlaces[{get_next_port(context + '_activate', 'out')}]", 
                                f"{context}.inTransition[{get_next_port(context, 'in')}]"))
            connections.append((f"{context}.outTransition[{get_next_port(context, 'out')}]", 
                                f"{deactivate}.inPlaces[{get_next_port(context + '_deactivate', 'in')}]"))
            
        # Generate connections for weak inclusions
        for source, target in self.weak_inclusions:
            duplicate_name = get_unique_name("duplicates", f"{source}_deactivate_{target}")
            inhibitor_name = get_unique_name("inhibitors", f"IA_{source}_{target}_weakInclusion")

            connections.extend([
                # Connect source place to duplicate deactivation transition of the source place
                (f"{source}.outTransition[{get_next_port(source, 'out')}]", f"{duplicate_name}.inPlaces[1]"),
                # Connect target place to duplicate deactivation transition of the source place via inhibitor arc
                (f"{target}.outTransition[{get_next_port(target, 'out')}]", f"{inhibitor_name}.inPlace"),
                (f"{inhibitor_name}.outTransition", f"{duplicate_name}.inPlaces[2]"),
                # Connect target place to the deactivation transition of the source place
                (f"{target}.outTransition[{get_next_port(target, 'out')}]", f"{source}_deactivate.inPlaces[{get_next_port(source + '_deactivate', 'in')}]"),
                # Connect activation transition of the source place to the target place
                (f"{source}_activate.outPlaces[{get_next_port(source + '_activate', 'out')}]", f"{target}.inTransition[{get_next_port(target, 'in')}]")
            ])

        # Generate connections for strong inclusions
        for source, target in self.strong_inclusions:
            duplicate_name = get_unique_name("duplicates", f"{target}_deactivate_{source}")
            inhibitor_name = get_unique_name("inhibitors", f"IA_{source}_{target}_strongInclusion")

            connections.extend([
                # Connect target place to duplicate deactivation transition of the source place
                (f"{target}.outTransition[{get_next_port(target, 'out')}]", f"{duplicate_name}.inPlaces[1]"),
                # Connect source place to duplicate deactivation transition of the source place via inhibitor arc
                (f"{source}.outTransition[{get_next_port(source, 'out')}]", f"{inhibitor_name}.inPlace"),
                (f"{inhibitor_name}.outTransition", f"{duplicate_name}.inPlaces[2]"),
                # Connect source place to deactivation transition of the target place
                (f"{source}.outTransition[{get_next_port(source, 'out')}]", f"{target}_deactivate.inPlaces[{get_next_port(target + '_deactivate', 'in')}]"),
                # Connect activation transition of the source place to the target place
                (f"{source}_activate.outPlaces[{get_next_port(source + '_activate', 'out')}]", f"{target}.inTransition[{get_next_port(target, 'in')}]")
            ])

        # Generate connections for exclusions
        for exclusion_group in self.exclusions:
            # Iterate over each context in the group
            for source in exclusion_group:
            # For the current source context, connect its place to the activation transitions of all other contexts
                for target in exclusion_group:
                    if source != target:  # Prevent self-connections
                        inhibitor_name = get_unique_name("inhibitors", f"IA_{source}_{target}_exclusion")
                        
                        # Connect place to the other activation transition via inhibitor arc
                        connections.extend([
                            (f"{source}.outTransition[{get_next_port(source, 'out')}]", f"{inhibitor_name}.inPlace"),
                            (f"{inhibitor_name}.outTransition", f"{target}_activate.inPlaces[{get_next_port(target + '_activate', 'in')}]")
                        ])

        # Requirement relation
        for source, target in self.requirements:
            duplicate_name = get_unique_name("duplicates", f"{source}_deactivate_{target}")
            inhibitor_name = get_unique_name("inhibitors", f"IA_{source}_{target}_requirement")

            connections.extend([
                # Connect source place to activation transition of the target place
                (f"{source}.outTransition[{get_next_port(source, 'out')}]", f"{target}_activate.inPlaces[{get_next_port(target + '_activate', 'in')}]"),
                # Connect source place to duplicate deactivation transition of the source place
                (f"{source}.outTransition[{get_next_port(source, 'out')}]", f"{duplicate_name}.inPlaces[1]"),
                # Connect activation transition of the target place to the source place
                (f"{target}_activate.outPlaces[{get_next_port(target + '_activate', 'out')}]", f"{source}.inTransition[{get_next_port(source, 'in')}]"),
                # Connect target place to duplicated deactivation transition of the source place
                (f"{target}.outTransition[{get_next_port(target, 'out')}]", f"{duplicate_name}.inPlaces[2]"),
                # Connect target place to the deactivation transition of the source place via inhibitor arc
                (f"{target}.outTransition[{get_next_port(target, 'out')}]", f"{inhibitor_name}.inPlace"),
                (f"{inhibitor_name}.outTransition", f"{source}_deactivate.inPlaces[{get_next_port(source + '_deactivate', 'in')}]")
            ])        

        # Render Petri Nets components
        for context in self.contexts:
            events = self.event_definitions[context]

            activation_time = events.get("activation_time", None)
            activation_condition = events.get("activation_condition", None)
            deactivation_time = events.get("deactivation_time", None)
            deactivation_condition = events.get("deactivation_condition", None)

            # Determine component types dynamically
            activation_component = "PNlib.Components.TE" if activation_time else "PNlib.Components.T"
            deactivation_component = "PNlib.Components.TE" if deactivation_time else "PNlib.Components.T"

            modelica_code.append(context_template.render(
                place=context,
                n_in=place_ports[context]["in"],
                n_out=place_ports[context]["out"],
                activate=f"{activation_component} {context}_activate",
                deactivate=f"{deactivation_component} {context}_deactivate",
                t_a_in=place_ports[f"{context}_activate"]["in"],
                t_a_out=place_ports[f"{context}_activate"]["out"],
                t_d_in=place_ports[f"{context}_deactivate"]["in"],
                activate_event=activation_time,
                activate_condition=activation_condition,
                deactivate_event=deactivation_time,
                deactivate_condition=deactivation_condition
            ))

        # Render Petri Nets components for weak inclusions
        for source, target in self.weak_inclusions:
            duplicate_name = get_unique_name("duplicates", f"{source}_deactivate_{target}")
            inhibitor_name = get_unique_name("inhibitors", f"IA_{source}_{target}_weakInclusion")
            
            # Determine the component type
            duplicate_event = self.event_definitions[source].get("deactivation_time", None)
            duplicate_component = "PNlib.Components.TE" if duplicate_event else "PNlib.Components.T"
            
            modelica_code.append(weak_inclusion_template.render(
                inhibitor=inhibitor_name,
                deactivate_duplicate=f"{duplicate_component} {duplicate_name}",
                deactivate_event=self.event_definitions[source].get("deactivation_time", None),
                deactivate_condition=self.event_definitions[source].get("deactivation_condition", None),
                duplicate_n_in=2
            ))

        # Render Petri Nets components for strong inclusions
        for source, target in self.strong_inclusions:
            duplicate_name = get_unique_name("duplicates", f"{target}_deactivate_{source}")
            inhibitor_name = get_unique_name("inhibitors", f"IA_{source}_{target}_strongInclusion")
            
            # Determine the component type
            duplicate_event = self.event_definitions[target].get("deactivation_time", None)
            duplicate_component = "PNlib.Components.TE" if duplicate_event else "PNlib.Components.T"

            modelica_code.append(strong_inclusion_template.render(
                inhibitor=inhibitor_name,
                deactivate_duplicate=f"{duplicate_component} {duplicate_name}",
                deactivate_event=self.event_definitions[source].get("deactivation_time", None),
                deactivate_condition=self.event_definitions[source].get("deactivation_condition", None),
                duplicate_n_in=2
            ))

        # Render Petri Nets components for exclusions
        for exclusion_group in self.exclusions:
            for source in exclusion_group:
                for target in exclusion_group:
                    if source != target:
                        inhibitor_name = get_unique_name("inhibitors", f"IA_{source}_{target}_exclusion")
                        
                        modelica_code.append(exclusion_template.render(
                            inhibitor=inhibitor_name
                        ))
        
        # Render Petri Nets components for requirements
        for source, target in self.requirements:
            duplicate_name = get_unique_name("duplicates", f"{source}_deactivate_{target}")
            inhibitor_name = get_unique_name("inhibitors", f"IA_{source}_{target}_requirement")
            
            # Determine the component type
            duplicate_event = self.event_definitions[source].get("deactivation_time", None)
            duplicate_component = "PNlib.Components.TE" if duplicate_event else "PNlib.Components.T"
            
            modelica_code.append(requirement_template.render(
                inhibitor=inhibitor_name,
                deactivate_duplicate=f"{duplicate_component} {duplicate_name}",
                deactivate_event=self.event_definitions[source].get("deactivation_time", None),
                deactivate_condition=self.event_definitions[source].get("deactivation_condition", None),
                duplicate_n_in=2
            ))

        # Render the final equation connections
        modelica_code.append(equation_template.render(connections=connections))
        return "\n".join(modelica_code), connections
    
    def visualize_petri_net(self, connections):
        """
        Generate a Petri Net diagram using graphviz with inhibitor arcs displayed cleanly.
        """
        dot = graphviz.Digraph(format='png', engine='dot', graph_attr={'rankdir': 'LR'})

        # Add nodes for places and transitions
        for context in self.contexts:
            events = event_definitions[context]
            activation_event = events.get("activation_time", None)
            deactivation_event = events.get("deactivation_time", None)
            activation_condition = events.get("activation_condition", None)
            deactivation_condition = events.get("deactivation_condition", None)

            # Format activation and deactivation details
            activation_info = f"Activation Time: {activation_event}" if activation_event else ""
            if activation_condition:
                activation_info += f"\nActivation Condition: {activation_condition}"

            deactivation_info = f"Deactivation Time: {deactivation_event}" if deactivation_event else ""
            if deactivation_condition:
                deactivation_info += f"\nDeactivation Condition: {deactivation_condition}"

            dot.node(context, shape='circle', style='filled', color='lightblue', label=f"{context}\n{activation_info}\n{deactivation_info}")
            dot.node(f"{context}_activate", shape='box', style='filled', color='lightgreen', label=f"{context}_activate")
            dot.node(f"{context}_deactivate", shape='box', style='filled', color='lightcoral', label=f"{context}_deactivate")

        # Process connections, handle inhibitor arcs
        for src, tgt in connections:
            if "IA_" in src:
                dot.edge(src.split(".")[0], tgt.split(".")[0], arrowhead="odot", style="solid")
            else:
                dot.edge(src.split(".")[0], tgt.split(".")[0], arrowhead="open", style="solid")

        # Save and render the graph
        dot.render('petri_net_visualization', view=True)
        print("Visualization saved as 'petri_net_visualization.png'")

    def visualize_context_relations(self):
        """
        Generate a diagram showing the relationships between contexts with specified styles for arrows.
        """
        dot = graphviz.Digraph(format='png', engine='dot', graph_attr={'rankdir': 'LR'}, name="context_relations")

        # Add nodes for all contexts with curved rectangular shapes
        for context in self.contexts:
            dot.node(context, shape='rect', style='rounded,filled', color='lightblue', label=context)

        # Add edges for weak inclusions with empty arrowheads
        for source, target in weak_inclusions:
            dot.edge(source, target, label="Weak Inclusion", arrowhead="open", color="black", style="solid")

        # Add edges for strong inclusions with filled arrowheads
        for source, target in strong_inclusions:
            dot.edge(source, target, label="Strong Inclusion", arrowhead="empty", color="black", style="solid")

        # Add edges for exclusions with "obox" arrowheads and arrowtails
        exclusion_pairs = set()
        for exclusion_group in exclusions:
            for i, source in enumerate(exclusion_group):
                for target in exclusion_group[i + 1:]:
                    pair = tuple(sorted([source, target]))  # Ensure unique unordered pairs
                    if pair not in exclusion_pairs:
                        exclusion_pairs.add(pair)
                        dot.edge(source, target, arrowhead='obox', dir='both', color='black', arrowtail='obox', label="Exclusion")

        # Add edges for requirements with "inv" arrowheads
        for source, target in requirements:
            dot.edge(target, source, label="Requirement", arrowhead="inv", color="black", style="solid")

        # Save and display the diagram
        dot.render('context_relations_diagram', view=True)
        print("Context relation diagram saved as 'context_relations_diagram.png'")

    def run(self, show_petri_net=True, show_relations=True):
        """Run the generator."""
        modelica_code, connections = self.generate_contexts()
        print(modelica_code)
        if show_petri_net:
            self.visualize_petri_net(connections)
        if show_relations:
            self.visualize_context_relations()

if __name__ == "__main__":
    """Example usage."""
    # Define contexts and relations
    # contexts = ["Pendulum", "FreeFlying"]
    contexts = ["hybridSupply", "greenSupply", "highPerformanceMode", "normalMode", "energySavingMode"]

    weak_inclusions = [
        # ("energySavingMode", "normalMode"),
        # ("energySavingMode", "highPerformanceMode")
    ]

    strong_inclusions = [
        # ("idleMode", "maintenanceMode"),
        # ("energySavingMode", "highPerformanceMode")
    ]

    exclusions = [
        # ["Pendulum", "FreeFlying"]
        ["highPerformanceMode", "normalMode", "energySavingMode"],
        ["hybridSupply", "greenSupply"]
    ]

    requirements = [
        # A is the requirement of B
        ("hybridSupply", "highPerformanceMode")
    ]

    event_definitions = {
        # "Pendulum": {
        #     "activation_condition": "xxx"
        # },
        # "FreeFlying": {
        #     "activation_condition": "xxx",
        # }
        "hybridSupply":{
            "activation_condition": "(hydrogenProduction < 50)",
            "deactivation_condition": "(hydrogenProduction > 50)"
        },
        "greenSupply":{
            "activation_condition": "(hydrogenProduction > 50)",
            "deactivation_condition": "(hydrogenProduction < 50)"
        },
        "highPerformanceMode":{
            "activation_condition": "(loadDemand > 150)",
            "deactivation_condition": "(loadDemand < 150)"
        },
        "normalMode":{
            "activation_condition": "(loadDemand > 50 and loadDemand < 150)",
            "deactivation_condition": "(loadDemand < 50 or loadDemand > 150)"
        },
        "energySavingMode": {
            "activation_condition": "(loadDemand < 50)",
            "deactivation_condition": "(loadDemand > 50)"
        }
    }    

    # Create instance
    generator = CoPNCompositor(contexts, weak_inclusions, strong_inclusions, exclusions, requirements, event_definitions)

    # Run the generator and visualize both diagrams
    generator.run(show_petri_net=True, show_relations=True)
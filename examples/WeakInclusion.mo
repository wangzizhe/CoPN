model WeakInclusion
  PNlib.Components.PD P1(nIn = 1, nOut = 2, maxTokens = 1)  annotation(
    Placement(transformation(origin = {-6, 40}, extent = {{-10, -10}, {10, 10}})));
  PNlib.Components.PD P2(nIn = 2, nOut = 3)  annotation(
    Placement(transformation(origin = {-6, -4}, extent = {{-10, -10}, {10, 10}})));
  inner PNlib.Components.Settings settings(showCapacity = true, showTokenFlow = true)  annotation(
    Placement(transformation(origin = {-82, 82}, extent = {{-10, -10}, {10, 10}})));
  PNlib.Components.TE T1a(nOut = 2, event = {1, 4, 6}, nIn = 0)  annotation(
    Placement(transformation(origin = {-70, 40}, extent = {{-10, -10}, {10, 10}})));
  PNlib.Components.TE T2a(nOut = 1, event = {3})  annotation(
    Placement(transformation(origin = {-70, -4}, extent = {{-10, -10}, {10, 10}})));
  PNlib.Components.TE T1d(nIn = 2, event = {5}, nOut = 0)  annotation(
    Placement(transformation(origin = {70, 40}, extent = {{-10, -10}, {10, 10}})));
  PNlib.Components.TE T2d(nIn = 1, event = {6})  annotation(
    Placement(transformation(origin = {70, -4}, extent = {{-10, -10}, {10, 10}})));
  PNlib.Components.IA IA1 annotation(
    Placement(transformation(origin = {28, 18}, extent = {{-6.3, -2.2}, {6.3, 2.2}})));
  PNlib.Components.TE T1d1(event = {5}, nIn = 2, nOut = 0) annotation(
    Placement(transformation(origin = {54, 16}, extent = {{-10, -10}, {10, 10}})));
equation
  connect(T1a.outPlaces[1], P1.inTransition[1]) annotation(
    Line(points = {{-66, 40}, {-16, 40}}, thickness = 0.5));
  connect(P1.outTransition[1], T1d.inPlaces[1]) annotation(
    Line(points = {{4, 40}, {66, 40}}, thickness = 0.5));
  connect(T2a.outPlaces[1], P2.inTransition[1]) annotation(
    Line(points = {{-66, -4}, {-16, -4}}, thickness = 0.5));
  connect(P2.outTransition[1], T2d.inPlaces[1]) annotation(
    Line(points = {{4, -4}, {66, -4}}, thickness = 0.5));
  connect(T1a.outPlaces[2], P2.inTransition[2]) annotation(
    Line(points = {{-66, 40}, {-16, 40}, {-16, -4}}, thickness = 0.5));
  connect(P2.outTransition[2], T1d.inPlaces[2]) annotation(
    Line(points = {{4, -4}, {66, -4}, {66, 40}}, thickness = 0.5));
  connect(P2.outTransition[3], IA1.inPlace) annotation(
    Line(points = {{4, -4}, {20, -4}, {20, 18}}));
  connect(IA1.outTransition, T1d1.inPlaces[2]) annotation(
    Line(points = {{36, 18}, {50, 18}, {50, 16}}));
  connect(P1.outTransition[2], T1d1.inPlaces[1]) annotation(
    Line(points = {{4, 40}, {50, 40}, {50, 16}}, thickness = 0.5));
  annotation(
    uses(PNlib(version = "3.0.0")));
end WeakInclusion;

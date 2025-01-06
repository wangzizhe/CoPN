model Exclusion
  PNlib.Components.PD P1(nIn = 1, nOut = 2)  annotation(
    Placement(transformation(origin = {-6, 36}, extent = {{-10, -10}, {10, 10}})));
  PNlib.Components.PD P2(nIn = 1, nOut = 2)  annotation(
    Placement(transformation(origin = {-6, -46}, extent = {{-10, -10}, {10, 10}})));
  PNlib.Components.TE T1(nOut = 1, nIn = 1, event = {1, 6, 9})  annotation(
    Placement(transformation(origin = {-70, 36}, extent = {{-10, -10}, {10, 10}})));
  PNlib.Components.TE T2(nIn = 1, event = {3, 10})  annotation(
    Placement(transformation(origin = {62, 36}, extent = {{-10, -10}, {10, 10}})));
  PNlib.Components.TE T3(nOut = 1, nIn = 1, event = {2, 5})  annotation(
    Placement(transformation(origin = {-70, -46}, extent = {{-10, -10}, {10, 10}})));
  PNlib.Components.TE T4(nIn = 1, event = {8})  annotation(
    Placement(transformation(origin = {62, -46}, extent = {{-10, -10}, {10, 10}})));
  PNlib.Components.IA IA1 annotation(
    Placement(transformation(origin = {-8, 0}, extent = {{-6.3, -2.2}, {6.3, 2.2}}, rotation = 90)));
  PNlib.Components.IA IA2 annotation(
    Placement(transformation(origin = {-48, -14}, extent = {{-6.3, -2.2}, {6.3, 2.2}}, rotation = -90)));
equation
  connect(T1.outPlaces[1], P1.inTransition[1]) annotation(
    Line(points = {{-66, 36}, {-16, 36}}, thickness = 0.5));
  connect(T3.outPlaces[1], P2.inTransition[1]) annotation(
    Line(points = {{-66, -46}, {-16, -46}}, thickness = 0.5));
  connect(P2.outTransition[1], T4.inPlaces[1]) annotation(
    Line(points = {{4, -46}, {58, -46}}, thickness = 0.5));
  connect(P1.outTransition[1], T2.inPlaces[1]) annotation(
    Line(points = {{4, 36}, {58, 36}}, thickness = 0.5));
  connect(P2.outTransition[2], IA1.inPlace) annotation(
    Line(points = {{4, -46}, {-8, -46}, {-8, -7}}));
  connect(IA1.outTransition, T1.inPlaces[1]) annotation(
    Line(points = {{-8, 8}, {-74, 8}, {-74, 36}}));
  connect(P1.outTransition[2], IA2.inPlace) annotation(
    Line(points = {{4, 36}, {-48, 36}, {-48, -7}}));
  connect(IA2.outTransition, T3.inPlaces[1]) annotation(
    Line(points = {{-48, -21}, {-74, -21}, {-74, -46}}));

annotation(
    uses(PNlib(version = "3.0.0")));
end Exclusion;

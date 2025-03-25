model StrongInclusion
  PNlib.Components.PD P1(maxTokens = 1, nIn = 1, nOut = 3, startTokens = 0) annotation(
    Placement(transformation(origin = {-24, 40}, extent = {{-10, -10}, {10, 10}})));
  PNlib.Components.PD P2(maxTokens = 1, nIn = 2, nOut = 2, startTokens = 0) annotation(
    Placement(transformation(origin = {-24, -38}, extent = {{-10, -10}, {10, 10}})));
  PNlib.Components.TE T1a(event = {1}, nIn = 0, nOut = 2) annotation(
    Placement(transformation(origin = {-64, 40}, extent = {{-10, -10}, {10, 10}})));
  PNlib.Components.TE T2a(event = {3}, nOut = 1) annotation(
    Placement(transformation(origin = {-64, -38}, extent = {{-10, -10}, {10, 10}})));
  PNlib.Components.TE T1d(event = {5}, nIn = 1, nOut = 0) annotation(
    Placement(transformation(origin = {68, 40}, extent = {{-10, -10}, {10, 10}})));
  PNlib.Components.TE T2d(event = {6}, nIn = 2) annotation(
    Placement(transformation(origin = {70, -38}, extent = {{-10, -10}, {10, 10}})));
  PNlib.Components.TE T2d1(event = {6}, nIn = 2) annotation(
    Placement(transformation(origin = {22, 0}, extent = {{-10, -10}, {10, 10}})));
  PNlib.Components.IA IA1 annotation(
    Placement(transformation(origin = {2, 22}, extent = {{-6.3, -2.2}, {6.3, 2.2}})));
equation
  connect(T1a.outPlaces[1], P1.inTransition[1]) annotation(
    Line(points = {{-60, 40}, {-34, 40}}, thickness = 0.5));
  connect(T1a.outPlaces[2], P2.inTransition[2]) annotation(
    Line(points = {{-60, 40}, {-34, 40}, {-34, -38}}, thickness = 0.5));
  connect(T2a.outPlaces[1], P2.inTransition[1]) annotation(
    Line(points = {{-60, -38}, {-34, -38}}, thickness = 0.5));
  connect(P2.outTransition[1], T2d.inPlaces[1]) annotation(
    Line(points = {{-14, -38}, {65, -38}}, thickness = 0.5));
  connect(P2.outTransition[2], T2d1.inPlaces[2]) annotation(
    Line(points = {{-14, -38}, {18, -38}, {18, 0}}, thickness = 0.5));
  connect(P1.outTransition[1], T1d.inPlaces[1]) annotation(
    Line(points = {{-14, 40}, {64, 40}}, thickness = 0.5));
  connect(P1.outTransition[2], T2d.inPlaces[2]) annotation(
    Line(points = {{-14, 40}, {66, 40}, {66, -38}}, thickness = 0.5));
  connect(P1.outTransition[3], IA1.inPlace) annotation(
    Line(points = {{-14, 40}, {-6, 40}, {-6, 22}}));
  connect(IA1.outTransition, T2d1.inPlaces[1]) annotation(
    Line(points = {{10, 22}, {18, 22}, {18, 0}}));
  annotation(
    uses(PNlib(version = "3.0.0")));
end StrongInclusion;

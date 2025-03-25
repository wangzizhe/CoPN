model Requirement
  PNlib.Components.PD P1(nIn = 2, nOut = 3)  annotation(
    Placement(transformation(origin = {-6, 44}, extent = {{-10, -10}, {10, 10}})));
  PNlib.Components.TE T1a(event = {3}, nOut = 1)  annotation(
    Placement(transformation(origin = {-68, 44}, extent = {{-10, -10}, {10, 10}})));
  PNlib.Components.TE T1d(nIn = 2, event = {6})  annotation(
    Placement(transformation(origin = {76, 44}, extent = {{-10, -10}, {10, 10}})));
  PNlib.Components.PD P2(nIn = 1, nOut = 3)  annotation(
    Placement(transformation(origin = {10, -52}, extent = {{-10, -10}, {10, 10}})));
  PNlib.Components.TE T2a(event = {2, 4}, nIn = 1, nOut = 2)  annotation(
    Placement(transformation(origin = {-68, -52}, extent = {{-10, -10}, {10, 10}})));
  PNlib.Components.TE T2d(event = {5}, nIn = 1)  annotation(
    Placement(transformation(origin = {76, -54}, extent = {{-10, -10}, {10, 10}})));
  PNlib.Components.TE T2d1(event = {6}, nIn = 2)  annotation(
    Placement(transformation(origin = {76, 12}, extent = {{-10, -10}, {10, 10}})));
  PNlib.Components.IA IA1 annotation(
    Placement(transformation(origin = {28, -20}, extent = {{-6.3, -2.2}, {6.3, 2.2}}, rotation = 90)));
equation
  connect(T1a.outPlaces[1], P1.inTransition[1]) annotation(
    Line(points = {{-64, 44}, {-16, 44}}, thickness = 0.5));
  connect(P1.outTransition[1], T2a.inPlaces[1]) annotation(
    Line(points = {{4, 44}, {-72, 44}, {-72, -52}}, thickness = 0.5));
  connect(P1.outTransition[2], T1d.inPlaces[1]) annotation(
    Line(points = {{4, 44}, {72, 44}}, thickness = 0.5));
  connect(T2a.outPlaces[2], P1.inTransition[2]) annotation(
    Line(points = {{-64, -52}, {-16, -52}, {-16, 44}}, thickness = 0.5));
  connect(T2a.outPlaces[1], P2.inTransition[1]) annotation(
    Line(points = {{-64, -52}, {0, -52}}, thickness = 0.5));
  connect(P2.outTransition[1], T2d.inPlaces[1]) annotation(
    Line(points = {{20, -52}, {72, -52}, {72, -54}}, thickness = 0.5));
  connect(P2.outTransition[2], T2d1.inPlaces[1]) annotation(
    Line(points = {{20, -52}, {72, -52}, {72, 12}}, thickness = 0.5));
  connect(P2.outTransition[3], IA1.inPlace) annotation(
    Line(points = {{20, -52}, {28, -52}, {28, -28}}));
  connect(IA1.outTransition, T1d.inPlaces[2]) annotation(
    Line(points = {{28, -12}, {72, -12}, {72, 44}}));
  connect(P1.outTransition[3], T2d1.inPlaces[2]) annotation(
    Line(points = {{4, 44}, {72, 44}, {72, 12}}, thickness = 0.5));
  annotation(
    uses(PNlib(version = "3.0.0")));
end Requirement;

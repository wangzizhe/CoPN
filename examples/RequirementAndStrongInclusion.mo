model RequirementAndStrongInclusion
  PNlib.Components.PD P1(nIn = 2, nOut = 3) annotation(
    Placement(transformation(origin = {6, 82}, extent = {{-10, -10}, {10, 10}})));
  PNlib.Components.TE T1a(event = {2}, nOut = 1) annotation(
    Placement(transformation(origin = {-68, 82}, extent = {{-10, -10}, {10, 10}})));
  PNlib.Components.TE T1d(event = {18}, nIn = 2) annotation(
    Placement(transformation(origin = {76, 82}, extent = {{-10, -10}, {10, 10}})));
  PNlib.Components.PD P2(nIn = 1, nOut = 5) annotation(
    Placement(transformation(origin = {8, -14}, extent = {{-10, -10}, {10, 10}})));
  PNlib.Components.TE T2a(event = {1, 3, 6, 15}, nIn = 1, nOut = 3) annotation(
    Placement(transformation(origin = {-68, -14}, extent = {{-10, -10}, {10, 10}})));
  PNlib.Components.TE T1d1(event = {18}, nIn = 3) annotation(
    Placement(transformation(origin = {40, 42}, extent = {{-10, -10}, {10, 10}})));
  PNlib.Components.TE T2d(event = {8}, nIn = 1) annotation(
    Placement(transformation(origin = {76, -16}, extent = {{-10, -10}, {10, 10}})));
  PNlib.Components.IA IA1 annotation(
    Placement(transformation(origin = {28, 18}, extent = {{-6.3, -2.2}, {6.3, 2.2}}, rotation = 90)));
  PNlib.Components.TE T3a(event = {1}, nIn = 0, nOut = 1) annotation(
    Placement(transformation(origin = {-68, -102}, extent = {{-10, -10}, {10, 10}})));
  PNlib.Components.TE T3d(event = {4}, nIn = 2, nOut = 0) annotation(
    Placement(transformation(origin = {76, -100}, extent = {{-10, -10}, {10, 10}})));
  PNlib.Components.TE T3d1(event = {2, 4}, nIn = 2, nOut = 0) annotation(
    Placement(transformation(origin = {38, -64}, extent = {{-10, -10}, {10, 10}})));
  PNlib.Components.PD P3(nIn = 2, nOut = 3) annotation(
    Placement(transformation(origin = {10, -104}, extent = {{-10, -10}, {10, 10}})));
  PNlib.Components.IA IA2 annotation(
    Placement(transformation(origin = {20, -40}, extent = {{-6.3, -2.2}, {6.3, 2.2}}, rotation = -90)));
equation
  connect(T1a.outPlaces[1], P1.inTransition[1]) annotation(
    Line(points = {{-63.2, 82}, {-5, 82}}, thickness = 0.5));
  connect(P1.outTransition[1], T2a.inPlaces[1]) annotation(
    Line(points = {{17, 82}, {-69, 82}, {-69, -14}, {-71.2, -14}}, thickness = 0.5));
  connect(P1.outTransition[2], T1d.inPlaces[1]) annotation(
    Line(points = {{17, 82}, {72.8, 82}}, thickness = 0.5));
  connect(T2a.outPlaces[2], P1.inTransition[2]) annotation(
    Line(points = {{-63.2, -14}, {-15.2, -14}, {-15.2, 82}, {-5, 82}}, thickness = 0.5));
  connect(T2a.outPlaces[1], P2.inTransition[1]) annotation(
    Line(points = {{-63.2, -14}, {-3, -14}}, thickness = 0.5));
  connect(P2.outTransition[1], T2d.inPlaces[1]) annotation(
    Line(points = {{19, -14}, {71, -14}, {71, -16}, {72.8, -16}}, thickness = 0.5));
  connect(P2.outTransition[2], T1d1.inPlaces[1]) annotation(
    Line(points = {{19, -14}, {72.8, -14}, {72.8, 42}, {35, 42}}, thickness = 0.5));
  connect(P2.outTransition[3], IA1.inPlace) annotation(
    Line(points = {{19, -14}, {27, -14}, {27, 10}, {28.8, 10}}));
  connect(IA1.outTransition, T1d.inPlaces[2]) annotation(
    Line(points = {{28, 25.3}, {72, 25.3}, {72, 81.3}}));
  connect(P1.outTransition[3], T1d1.inPlaces[2]) annotation(
    Line(points = {{17, 82}, {72.8, 82}, {72.8, 42}, {35, 42}}, thickness = 0.5));
  connect(T2a.outPlaces[3], P3.inTransition[1]) annotation(
    Line(points = {{-64, -14}, {0, -14}, {0, -104}}, thickness = 0.5));
  connect(T3a.outPlaces[1], P3.inTransition[2]) annotation(
    Line(points = {{-64, -102}, {0, -102}, {0, -104}}, thickness = 0.5));
  connect(P2.outTransition[4], T3d.inPlaces[1]) annotation(
    Line(points = {{18, -14}, {72, -14}, {72, -100}}, thickness = 0.5));
  connect(P2.outTransition[5], IA2.inPlace) annotation(
    Line(points = {{18, -14}, {20, -14}, {20, -32}}));
  connect(IA2.outTransition, T3d1.inPlaces[1]) annotation(
    Line(points = {{20, -48}, {34, -48}, {34, -64}}));
  connect(P3.outTransition[2], T3d1.inPlaces[2]) annotation(
    Line(points = {{20, -104}, {34, -104}, {34, -64}}, thickness = 0.5));
  connect(P3.outTransition[3], T3d.inPlaces[2]) annotation(
    Line(points = {{20, -104}, {72, -104}, {72, -100}}, thickness = 0.5));
  connect(P3.outTransition[1], T1d1.inPlaces[3]) annotation(
    Line(points = {{20, -104}, {36, -104}, {36, 42}}, thickness = 0.5));
  annotation(
    Diagram);
end RequirementAndStrongInclusion;

#!/usr/bin/python

# Copyright (C) 2016 Jesse Moseman, and John Carlo B. Viernes IV
#
# This file is part of fossologyFunTime.
#
# fossologyFunTime is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# fossologyFunTime is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with fossologyFunTime.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-2.0+

import networkx

graph=networkx.read_graphml("test.graphml")
nodesDict=dict(graph.nodes(data="NodeLabel"))
edgeLabels=[]
for e1,e2 in graph.edges():
	edgeLabels.append((nodesDict[e1]['label'],nodesDict[e2]['label']))

for e in edgeLabels:
	print e

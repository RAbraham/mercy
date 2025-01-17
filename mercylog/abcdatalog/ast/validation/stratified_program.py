# import abcdatalog.ast.PredicateSym;
from mercylog.abcdatalog.ast.predicate_sym import PredicateSym
#
# /**
#  * A Datalog program that has been stratified; for instance, to support
#  * stratified negation.
#  *
#  */
from abc import ABC, abstractmethod
from typing import *
class StratifiedProgram(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def getStrata(self) -> List[Set[PredicateSym]]:
        pass

    @abstractmethod
    def getPredToStratumMap(self) -> Dict[PredicateSym, int]:
        pass
# public interface StratifiedProgram extends UnstratifiedProgram {
# 	List<Set<PredicateSym>> getStrata();
#
# 	Map<PredicateSym, Integer> getPredToStratumMap();
# }
# /*******************************************************************************
#  * This file is part of the AbcDatalog project.
#  *
#  * Copyright (c) 2016, Harvard University
#  * All rights reserved.
#  *
#  * This program and the accompanying materials are made available under
#  * the terms of the BSD License which accompanies this distribution.
#  *
#  * The development of the AbcDatalog project has been supported by the
#  * National Science Foundation under Grant Nos. 1237235 and 1054172.
#  *
#  * See README for contributors.
#  ******************************************************************************/
# package abcdatalog.ast.validation;
#
# import java.util.List;
# import java.util.Map;
# import java.util.Set;
#
# import abcdatalog.ast.PredicateSym;
#
# /**
#  * A Datalog program that has been stratified; for instance, to support
#  * stratified negation.
#  *
#  */
# public interface StratifiedProgram extends UnstratifiedProgram {
# 	List<Set<PredicateSym>> getStrata();
#
# 	Map<PredicateSym, Integer> getPredToStratumMap();
# }

from abc import ABCMeta,abstractmethod
from typing import TypeVar
#==========モノイド
MonoidType=TypeVar("MonoidType", bound="Monoid")
class Monoid(metaclass=ABCMeta):
    @abstractmethod
    def __mul__(self:MonoidType,other:MonoidType)->MonoidType:
        pass

    @abstractmethod
    def identity(self:MonoidType) -> MonoidType:
        pass

    @abstractmethod
    def __eq__(self,other):
        pass
#==========群
GroupType=TypeVar("GroupType", bound="Group")
class Group(Monoid,metaclass=ABCMeta):
    @abstractmethod
    def inverse(self:GroupType) -> GroupType:
        pass
#==========加法群
AdditiveGroupType = TypeVar("AdditiveGroupType", bound="AdditiveGroup")
class AdditiveGroup(metaclass=ABCMeta):
    @abstractmethod
    def __add__(self:AdditiveGroupType, other:AdditiveGroupType) -> AdditiveGroupType:
        pass

    @abstractmethod
    def zero(self:AdditiveGroupType) -> AdditiveGroupType:
        pass

    @abstractmethod
    def __neg__(self:AdditiveGroupType) -> AdditiveGroupType:
        pass

    def __sub__(self:AdditiveGroupType, other:AdditiveGroupType) -> AdditiveGroupType:
        return self+(-other)

    @abstractmethod
    def __eq__(self:AdditiveGroupType, other:AdditiveGroupType) -> AdditiveGroupType:
        pass
#==========環
RingType=TypeVar("RingType", bound="Ring")
class Ring(AdditiveGroup,Monoid):
    pass

    
    
class R(Ring):
    def __init__(self,x):
        self.x=x

    def __repr__(self):
        return str(self.x)

    def __add__(self,other):
        return R(self.x+other.x)

    def __mul__(self,other):
        return R(self.x*other.x)

    def __eq__(self,other):
        return self.x==other.x

    def __neg__(self):
        return R(-self.x)

    def identity(self):
        return R(1)

    def zero(self):
        return R(0)

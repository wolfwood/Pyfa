# setBonusChristmasCapacitorCapacity
#
# Used by:
# Implants named like: Genolution Core Augmentation CA (4 of 4)
runTime = "early"
type = "passive"
def handler(fit, implant, context):
    fit.appliedImplants.filteredItemMultiply(lambda mod: mod.item.group.name == "Cyberimplant",
                                      "capacitorCapacityBonus", implant.getModifiedItemAttr("implantSetChristmas"))

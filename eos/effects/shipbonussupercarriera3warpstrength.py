# shipBonusSupercarrierA3WarpStrength
#
# Used by:
# Ship: Aeon
# Ship: Revenant
type = "passive"
def handler(fit, src, context):
    fit.ship.increaseItemAttr("warpScrambleStatus", src.getModifiedItemAttr("shipBonusSupercarrierA3"), skill="Amarr Carrier")

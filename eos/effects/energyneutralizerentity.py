# energyNeutralizerEntity
#
# Used by:
# Drones from group: Energy Neutralizer Drone (3 of 3)
from eos.types import State
type = "active", "projected"
def handler(fit, container, context):
    if "projected" in context and ((hasattr(container, "state") \
    and container.state >= State.ACTIVE) or hasattr(container, "amountActive")):
        amount = container.getModifiedItemAttr("energyDestabilizationAmount")
        time = container.getModifiedItemAttr("duration")
        fit.addDrain(time, amount, 0)

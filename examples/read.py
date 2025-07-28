import time

from models.scheduler import Schedule
from service import deserializer, serializer

t = time.time()
sch = Schedule(
    events=serializer.read_exel("GAL_NORD_5var_ok3_value.xlsx"),
)
deserializer.to_eclipse_ascii(sch)

print(time.time() - t)

pass

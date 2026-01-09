import time

import schedulercore

t = time.time()
sch = schedulercore.Schedule(
    events=schedulercore.read_exel("name.xlsx"),
)
schedulercore.to_eclipse_ascii(sch)

print(time.time() - t)

pass

#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-2.0-only

import raw_pylibcpupower as p

# Simple function call

"""
Get cstate count
"""
cpu_cstates_count = p.cpuidle_state_count(0)
if cpu_cstates_count > -1:
    print(f"CPU 0 has {cpu_cstates_count} c-states")
else:
    print(f"cstate count error: return code: {cpu_cstates_count}")

"""
Disable cstate (will fail if the above returns is under 1, ex: a virtual machine)
"""
cstate_disabled = p.cpuidle_state_disable(0, 0, 1)

match cstate_disabled:
    case 0:
        print(f"CPU state disabled")
    case -1:
        print(f"Idlestate not available")
    case -2:
        print(f"Disabling is not supported by the kernel")
    case -3:
        print(f"No write access to disable/enable C-states: try using sudo")
    case _:
        print(f"Not documented: {cstate_disabled}")

"""
Test cstate is disabled
"""
is_cstate_disabled = p.cpuidle_is_state_disabled(0, 0)

match is_cstate_disabled:
    case 1:
        print(f"CPU is disabled")
    case 0:
        print(f"CPU is enabled")
    case -1:
        print(f"Idlestate not available")
    case -2:
        print(f"Disabling is not supported by kernel")
    case _:
        print(f"Not documented: {is_cstate_disabled}")

# Pointer example

topo = p.cpupower_topology()
total_cpus = p.get_cpu_topology(topo)
if total_cpus > 0:
    print(f"Number of total cpus: {total_cpus} and number of cores: {topo.cores}")
else:
    print(f"Error: could not get cpu topology")

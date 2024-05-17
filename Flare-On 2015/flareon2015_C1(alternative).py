import angr
proj=angr.Project("i_am_happy_you_are_to_playing_the_flareon_challenge.exe")
state =proj.factory.full_init_state(args="./i_am_happy_you_are_to_playing_the_flareon_challenge.exe")
state.memory.store(0x402158, state.solver.BVS("ans", 8*40))
sim_manager=proj.factory.simulation_manager(state)
sim_manager.explore(find=0x401063,avoid=0x40107b)
found_state=sim_manager.found[0]
print(found_state.solver.eval(found_state.memory.load(0x402158, 40), cast_to=bytes).strip(b'\0'))

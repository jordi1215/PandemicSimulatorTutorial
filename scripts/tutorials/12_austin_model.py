# Confidential, Copyright 2020, Sony Corporation of America, All rights reserved.
from tqdm import trange

import pandemic_simulator as ps


def run_pandemic_sim() -> None:
    """Here we execute the simulator using austin regulations, Austin config and default person routines."""

    print('\nA tutorial that runs the simulator using austin regulations and default person routines', flush=True)

    # init globals
    ps.init_globals(seed=1)

    # select a simulator config
    #sim_config = ps.sh.austin_config
    # run two expriments
    sim_config = ps.sh.small_town_config
    sim_config = ps.sh.town_config

    # make sim
    sim = ps.env.PandemicSim.from_config(sim_config)

    # wrap = ps.env.PandemicGymEnv.from_config(sim_config=sim_config, pandemic_regulations=ps.sh.austin_regulations)

    # setup viz to show plots
    viz = ps.viz.SimViz.from_config(sim_config)

    # impose a regulation
    # sim.impose_regulation(regulation=ps.sh.austin_regulations[0])  # stage 0
    action = 0
    Reward = 0
    # run regulation steps in the simulator
    for day in trange(120, desc='Simulating day'):
        # for day in trange(120, desc='Simulating day'):
        if day == 40:
            sim.impose_regulation(regulation=ps.sh.austin_regulations[1])
        if day == 70:
            sim.impose_regulation(regulation=ps.sh.austin_regulations[2])
        sim.step_day()
        #obs, reward, _, _ = wrap.step(action=int(action))
        #Reward += reward
        viz.record(sim.state)
        # viz.record(reward)

    # generate plots
    viz.plot()
    # print('Reward:'+str(Reward))


if __name__ == '__main__':
    run_pandemic_sim()

import gymnasium as gym

env = gym.make('Skiing-v5', render_mode='human')
obs, info = env.reset()
done = False
#array
while not done:
    action = env.action_space.sample()  
    obs, rew, done, truncated, info = env.step(action)
    #record obs, rew, info
    if done or truncated:
        obs, info = env.reset()
    
env.close()

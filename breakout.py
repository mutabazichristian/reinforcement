import gymnasium as gym

env = gym.make('FrozenLake-v1', render_mode='human')   
obs, info = env.reset()                           

max_steps = 20                                     
terminated = False
truncated = False

for step in range(max_steps):                    
    action = env.action_space.sample()             
    obs, reward, terminated, truncated, info = env.step(action)  

    print(f"Step: {step + 1}, Action: {action}, Reward: {reward}")

    if terminated or truncated:                   
        print("Episode ended.")                  
        break

env.close()                                        

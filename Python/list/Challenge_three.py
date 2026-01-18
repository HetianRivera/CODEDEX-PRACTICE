# Google the Best Picture winners from 2020, 2021, 2022, 2023, and 2024. Then, add them to the front of the best_pictures list.

# Lastly, print the best_pictures list. Make sure that the updated list starts with the winner for 2024, then 2023, then 2022, then 2021, then 2020, and so on.

# Note: Make sure to match the format of the existing list. And remember, it's the year of the movie, not the year of the ceremony.

best_pictures = [
  '2019 - Parasite',
  '2018 - Green Book',
  '2017 - The Shape of Water',
  '2016 - Moonlight',
  '2015 - Spotlight',
  '2014 - Birdman',
  '2013 - 12 Years a Slave',
  '2012 - Argo',
  '2011 - The Artist'
]

best_pictures.insert(0, '2020 - Nomadland')
best_pictures.insert(0, '2021 - CODA')
best_pictures.insert(0, '2022 - Everything Everywhere All at Once')
best_pictures.insert(0, '2023 - Oppenheimer')
best_pictures.insert(0, '2024 - Anora')

for i in range(len(best_pictures)):
    print(best_pictures[i])
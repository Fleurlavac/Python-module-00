"""
Auteur : fcaval@student.42lehavre.fr
Date : 05/01/26
"""

def ft_count_harvest_recursive(n, current=1):
    if current > n: 
        print("Harvest time!")
        return

    print(f"Day {current}")
    ft_count_harvest_recursive(n, current + 1)

from models import Problem, Solution


def solve(problem: Problem) -> Solution:
    popularity_counts = {ing: 0 for ing in problem.ingredients}
    for client in problem.clients:
        for ing in client.likes:
            popularity_counts[ing] += 1
        for ing in client.dislikes:
            popularity_counts[ing] -= 1
    pizza = set()
    for ing, count in popularity_counts.items():
        if count > 0:
            pizza.add(ing)
    score = 0
    for client in problem.clients:
        if client.likes.issubset(pizza) and client.dislikes.isdisjoint(pizza):
            score += 1
    return Solution(score=score, pizza=pizza)

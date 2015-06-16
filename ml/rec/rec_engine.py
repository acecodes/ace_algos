from math import sqrt

"""
A sample recommendation engine
Some code from "Programming Collective Intelligence" by Toby Segaran
"""


def sim_distance(prefs, person1, person2):
    """Distance-based similarity score for two people"""

    try:
        # Mutually-rated items
        similarities = {}
        for item in prefs[person1]:
            if item in prefs[person2]:
                similarities[item] = 1

        # Return 0 if they don't have any ratings in common
        if len(similarities) == 0:
            return 0

        sum_of_squares = sum(
            [pow(prefs[person1][item] - prefs[person2][item], 2)
             for item in similarities])

        return 1 / (1 + sqrt(sum_of_squares))

    except KeyError as e:
        return str(e) + ' is not a person within your dataset.'


def sim_pearson(prefs, person1, person2):
    """Similarities based on Pearson product moment correlation coefficient"""

    try:
        # Mutually-rated items
        similarities = {}
        for item in prefs[person1]:
            if item in prefs[person2]:
                similarities[item] = 1

        n = len(similarities)
        if n == 0:
            return 0

        # Sum up preferences
        sum1 = sum([prefs[person1][item] for item in similarities])
        sum2 = sum([prefs[person2][item] for item in similarities])

        # Sum up squares
        sum1_square = sum([pow(prefs[person1][item], 2)
                           for item in similarities])
        sum2_square = sum([pow(prefs[person2][item], 2)
                           for item in similarities])

        # Sum up products
        p_sum = sum([prefs[person1][item] * prefs[person2][item]
                     for item in similarities])

        num = p_sum - (sum1 * sum2 / n)

        density = sqrt(
            (sum1_square - pow(sum1, 2) / n) * (sum2_square - pow(sum2, 2) / n)
        )

        if density == 0:
            return 0

        r = num / density
        return r

    except KeyError as e:
        return str(e) + ' is not a person within your dataset.'


def transform_prefs(prefs):
    """Transform data so that similar items can be recommended"""
    result = {}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item, {})

            result[item][person] = prefs[person][item]
    return result


def top_matches(prefs, person, n=5, similarity=sim_pearson):
    """See which critics are the most similar to each other"""
    scores = [(similarity(prefs, person, other), other)
              for other in prefs if other != person]

    scores.sort()
    scores.reverse()
    return scores[0:n]


def get_recommendations(prefs, person, similarity=sim_pearson):
    """Generate recommendations for a person"""
    totals = {}
    similarity_sums = {}

    for other in prefs:
        if other == person:
            continue

        sim = similarity(prefs, person, other)

        if sim <= 0:
            continue

        for item in prefs[other]:
            if item not in prefs[person] or prefs[person][item] == 0:
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item] * sim
                similarity_sums.setdefault(item, 0)
                similarity_sums[item] += sim

    # Normalized list
    rankings = [(total / similarity_sums[item], item)
                for item, total in totals.items()]

    # Returns normalized score, not an r that would be between -1 and 1
    rankings.sort()
    rankings.reverse()
    return rankings


def calculate_similar_items(prefs, n=10):
    # Create a dictionary of items showing which other items they
    # are most similar to.
    result = {}

    # Invert the preference matrix to be item-centric
    item_prefs = transform_prefs(prefs)
    c = 0
    for item in item_prefs:
        # Status updates for large datasets
        c += 1
        if c % 100 == 0:
            print "%d / %d" % (c, len(item_prefs))
        # Find the most similar items to this one
        scores = top_matches(item_prefs, item, n=n, similarity=sim_distance)
        result[item] = scores
    return result

"""Sample data: Movie critics and their scores for movies"""
critics = {'Lisa Rose': {'Lady in the Water': 2.5,
                         'Snakes on a Plane': 3.5,
                         'Just My Luck': 3.0,
                         'Superman Returns': 3.5,
                         'You, Me and Dupree': 2.5,
                         'The Night Listener': 3.0},
           'Gene Seymour': {'Lady in the Water': 3.0,
                            'Snakes on a Plane': 3.5,
                            'Just My Luck': 1.5,
                            'Superman Returns': 5.0,
                            'The Night Listener': 3.0,
                            'You, Me and Dupree': 3.5},
           'Michael Phillips': {'Lady in the Water': 2.5,
                                'Snakes on a Plane': 3.0,
                                'Superman Returns': 3.5,
                                'The Night Listener': 4.0},
           'Claudia Puig': {'Snakes on a Plane': 3.5,
                            'Just My Luck': 3.0,
                            'The Night Listener': 4.5,
                            'Superman Returns': 4.0,
                            'You, Me and Dupree': 2.5},
           'Mick LaSalle': {'Lady in the Water': 3.0,
                            'Snakes on a Plane': 4.0,
                            'Just My Luck': 2.0,
                            'Superman Returns': 3.0,
                            'The Night Listener': 3.0,
                            'You, Me and Dupree': 2.0},
           'Jack Matthews': {'Lady in the Water': 3.0,
                             'Snakes on a Plane': 4.0,
                             'The Night Listener': 3.0,
                             'Superman Returns': 5.0,
                             'You, Me and Dupree': 3.5}
           }


if __name__ == '__main__':
    print('User-based collaborative filtering: ')
    print(sim_distance(critics, 'Claudia Puig', 'Mick LaSalle'))
    print('\nPerson correlation:')
    print(sim_pearson(critics, 'Claudia Puig', 'Mick LaSalle'))
    print('\nTop matches:')
    print(top_matches(critics, 'Jack Matthews'))
    print('\nRecommendations:')
    print(get_recommendations(critics, 'Michael Phillips'))
    movies = transform_prefs(critics)
    print('\nTop matches with transform:')
    print(top_matches(movies, 'Just My Luck'))
    print(get_recommendations(movies, 'Just My Luck'))
    print('Item-based collaborative filtering:')
    print(calculate_similar_items(critics))

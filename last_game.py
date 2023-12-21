'''
Permet d'afficher les résultats de la dernière partie
'''

SELECT (STRFTIME('%s', date_end) -STRFTIME('%s', date_start))/60 duration, alias, score
FROM game g
JOIN game_gamer gg ON gg.game_id = g.id  
WHERE id IN (SELECT MAX(id) FROM game)
ORDER BY score DESC

"""Module pour l'inteprétation des segments et la recommandation d'actions"""

STRATEGIES = {
    0: {
        "title": "Clients à haute valeur avec achats fréquents et récents",
        "description": "Ces clients ont la dépense totale la plus élevée, la fréquence d'achat la plus élevée, et des achats très récents. Ils achètent de nombreux articles et ont une valeur de fret élevée.",
        "actions": {
            "Programme VIP": "Créer un programme exclusif avec des avantages premium pour récompenser et retenir ces clients de grande valeur",
            "Service client personnalisé": "Offrir un service dédié pour répondre rapidement à leurs besoins et maintenir leur satisfaction",
            "Accès en avant-première": "Proposer un accès prioritaire aux nouveaux produits ou ventes pour stimuler leur engagement continu",
        },
    },
    1: {
        "title": "Clients occasionnels à valeur moyenne",
        "description": "Ces clients ont une dépense totale modérée, une fréquence d'achat plus basse, et des achats moins récents. Ils achètent moins d'articles mais ont un ratio de paiement fractionné plus élevé.",
        "actions": {
            "Campagnes de réactivation": "Envoyer des offres personnalisées basées sur leurs achats passés pour les inciter à revenir",
            "Options de paiement flexibles": "Mettre en avant les options de paiement échelonné pour encourager des achats plus importants",
            "Contenu engageant": "Partager du contenu pertinent pour maintenir la connexion avec la marque entre les achats",
        },
    },
    2: {
        "title": "Clients à valeur élevée avec achats importants mais peu fréquents",
        "description": "Ces clients ont une dépense totale élevée malgré une fréquence d'achat modérée. Ils effectuent des achats importants et ont une valeur de fret élevée.",
        "actions": {
            "Programmes de fidélité axés sur la valeur": "Récompenser la valeur totale des achats plutôt que la fréquence",
            "Ventes croisées et montées en gamme": "Suggérer des produits complémentaires ou haut de gamme lors de leurs visites",
            "Événements exclusifs": "Organiser des événements spéciaux pour ces clients à forte valeur pour renforcer leur relation avec la marque",
        },
    },
    3: {
        "title": "Nouveaux clients ou clients à faible engagement",
        "description": "Ces clients ont la dépense totale la plus faible, une basse fréquence d'achat, et des achats relativement récents. Ils achètent peu d'articles et ont une faible valeur de fret.",
        "actions": {
            "Programme d'onboarding": "Mettre en place un parcours d'accueil pour les nouveaux clients afin de les familiariser avec l'offre",
            "Offres de découverte": "Proposer des offres spéciales sur une gamme de produits pour encourager l'exploration de l'assortiment",
            "Enquêtes de satisfaction": "Recueillir des feedbacks pour comprendre leurs besoins et améliorer leur expérience",
        },
    },
    4: {
        "title": "Clients à très haute valeur avec achats fréquents et volumineux",
        "description": "Ces clients ont la dépense totale la plus élevée, la fréquence d'achat la plus élevée, et achètent le plus grand nombre d'articles. Ils ont aussi la valeur de fret la plus élevée.",
        "actions": {
            "Service ultra-premium": "Offrir un service de conciergerie dédié pour répondre à tous leurs besoins",
            "Co-création de produits": "Les impliquer dans le développement de nouveaux produits ou services",
            "Avantages exclusifs": "Proposer des avantages uniques comme la livraison gratuite à vie ou des remises permanentes pour maintenir leur fidélité",
        },
    },
    5: {
        "title": "Clients à faible valeur avec achats peu fréquents mais récents",
        "description": "Ces clients ont la deuxième dépense totale la plus faible, une fréquence d'achat basse, mais des achats relativement récents. Ils ont le ratio de paiement fractionné le plus élevé.",
        "actions": {
            "Offres d'encouragement": "Proposer des remises sur le prochain achat pour augmenter la fréquence",
            "Éducation sur les produits": "Fournir du contenu informatif pour augmenter la valeur perçue et justifier des achats plus importants",
            "Options de paiement flexibles": "Mettre en avant les facilités de paiement pour réduire les barrières à l'achat",
        },
    },
}

"""Module pour l'inteprétation des segments et la recommandation d'actions"""

STRATEGIES = {
    0: {
        "title": "Clients occasionnels avec faible dépense moyenne",
        "description": "Ces clients ont une dépense totale relativement faible, une fréquence d'achat basse, et un faible nombre d'articles achetés en moyenne. Leurs achats sont peu récents, et leur valeur de fret est également basse.",
        "actions": {
            "Réengagement": "Lancer des campagnes de réactivation ciblées, comme des offres promotionnelles ou des remises spéciales pour encourager ces clients à revenir",
            "Communication personnalisée": "Envoyer des emails ou des notifications pour rappeler à ces clients l'existence de la marque et proposer des produits qui correspondent à leurs précédents achats",
            "Programmes de fidélité": "Introduire un programme de fidélité qui incite ces clients à augmenter leur fréquence d'achat et leur panier moyen",
        },
    },
    1: {
        "title": "Clients achetant principalement en plusieurs fois avec faible fréquence",
        "description": "Ces clients dépensent un montant modéré mais leur fréquence d'achat est relativement faible. Ils optent souvent pour des paiements en plusieurs fois et achètent peu d'articles. Leur activité est assez récente et leur valeur de fret est modeste.",
        "actions": {
            "Offres sur les paiements fractionnés": "Promouvoir des options de paiement fractionné avec des conditions avantageuses pour attirer ces clients",
            "Ciblage de produits complémentaires": "Proposer des produits complémentaires ou accessoires pour augmenter leur panier moyen à chaque achat",
            "Campagnes de relance": "Envoyer des rappels et des offres limitées dans le temps pour les inciter à acheter plus fréquemment",
        },
    },
    2: {
        "title": "Clients à haute valeur avec achats fréquents et importants",
        "description": "Ce segment est constitué de clients à haute valeur avec la dépense totale la plus élevée et la fréquence d'achat la plus élevée. Ils achètent de nombreux articles et leur valeur de fret est également la plus élevée. Ces clients sont relativement récents.",
        "actions": {
            "Programme VIP": "Mettre en place un programme exclusif avec des avantages premium pour récompenser et retenir ces clients de grande valeur",
            "Service client personnalisé": "Offrir un service dédié pour répondre rapidement à leurs besoins et maintenir leur satisfaction",
            "Accès en avant-première": "Proposer un accès prioritaire aux nouveaux produits ou ventes pour stimuler leur engagement continu",
        },
    },
    3: {
        "title": "Clients réguliers avec paniers d'achat moyens",
        "description": "Ces clients ont une dépense totale relativement élevée et achètent régulièrement. Ils achètent un nombre modéré d'articles avec une valeur de fret assez élevée. Leur activité est également récente.",
        "actions": {
            "Offres groupées": "Proposer des offres groupées ou des réductions sur les achats multiples pour encourager ces clients à acheter davantage lors de chaque commande",
            "Emails de recommandation": "Envoyer des recommandations personnalisées basées sur leurs précédents achats pour augmenter la fréquence d'achat",
            "Programmes de fidélité": "Mettre en avant les avantages du programme de fidélité pour les inciter à continuer d'acheter régulièrement",
        },
    },
    4: {
        "title": "Clients récents et peu engagés",
        "description": "Ce segment comprend des clients avec une dépense totale faible et une fréquence d'achat basse. Ils achètent peu d'articles mais sont assez récents dans leur engagement. Leur valeur de fret est également faible.",
        "actions": {
            "Offres de bienvenue": "Lancer des campagnes de bienvenue pour ces clients récents avec des offres spéciales pour les inciter à effectuer de nouveaux achats",
            "Communication proactive": "Maintenir un contact régulier avec des suggestions de produits personnalisés pour les engager davantage",
            "Récompenses pour achat récurrent": "Proposer des remises ou des avantages supplémentaires pour encourager ces clients à acheter plus fréquemment",
        },
    },
}

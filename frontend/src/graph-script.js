const ctx = document.getElementById('myChart');

new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Auvergne-Rhône-Alpes', 'Bourgogne-Franche-Comtée', 'Bretagne', 'Centre-Val de Loire', 'Corse', 'Grand-Est', 'Hauts-de-France', 'Ile-de-France', 'Normandie', 'Nouvelle-Aquitaine', 'Occitanie', 'Pays de la Loire', "Provence Alpes Côte d'Azur"],
        datasets: [{
            label: 'Nombre de votants par région',
            data: [12, 19, 3, 5, 2, 3, 7, 25, 21, 9, 17, 10, 8],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
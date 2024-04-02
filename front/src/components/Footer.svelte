<footer>
    <div class="footer-center">
        <img class="footer-logo" src="/logo-2.png" alt="logo"/>
        <span class="title"> Saison électorale </span>
        <span>🌦️ / 🗳️ </span>
        <span> Un projet par <a href="https://github.com/gregglrnt"> @gregglrnt </a> et <a href="https://github.com/Mdetorquat"> @Mdetorquat </a> </span>
        <p> Sources : <mark><a href="https://www.data.gouv.fr/fr/pages/donnees-des-elections/">data.gouv.fr</a></mark> et <mark><a href="https://public.opendatasoft.com/explore/dataset/donnees-synop-essentielles-omm/table">SYNOP (Météo France)</a></mark> </p>
    </div>
</footer>

<style>
footer {
    background: var(--french-white-gradient);
    padding: 32px 0;
    margin-top: 32px;
}

.footer-center {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 16px;
}

.footer-logo {
    transform: rotate(90deg)
}

.title {
    font-family: 'Spectral', serif;
    font-size: 16px;
    font-weight: bold;
}

</style>
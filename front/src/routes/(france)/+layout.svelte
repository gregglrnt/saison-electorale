<script lang="ts">
    import {elections, currentElection} from "$lib/election";
</script>

<h1>Résultats pour le {$elections.find((e) => $currentElection === e.value)?.label} </h1>

async function getTimeVisitingAllAttractions(index) {
	const queryParam = new URLSearchParams({
		index: index,
	});
	const resJson = await fetch(
		getTimeVisitingAllAttractionsUrl + "?" + queryParam
	);
	const res = await resJson.json();

	if (res.status === 200) {
		document.getElementById("date-" + index.toString()).innerHTML = res.date;
		document.getElementById("is-visit-all-" + index.toString()).innerHTML =
			res.is_visit_all_attractions;
		document.getElementById("time-visit-all-" + index.toString()).innerHTML =
			res.time;
	} else {
        document.getElementById("date-" + index.toString()).innerHTML = 'no data';
		document.getElementById("is-visit-all-" + index.toString()).innerHTML =
			'no data';
		document.getElementById("time-visit-all-" + index.toString()).innerHTML =
			'no data';
    }
}

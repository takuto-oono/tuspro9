async function getTimeVisitingAllAttractions(model_id) {
	const queryParam = new URLSearchParams({
		model_id: model_id,
	});
	const resJson = await fetch(
		getTimeVisitingAllAttractionsUrl + "?" + queryParam
	);
	const res = await resJson.json();

	for (let index = 0; index < 7; index++) {
		document.getElementById(
			"date-" + index.toString() + "-" + model_id.toString()
		).innerHTML = res[index]["date"];

		document.getElementById(
			"route-date-" + index.toString() + "-" + model_id.toString()
		).innerHTML = res[index]["date"];

		if (res[index]["is_visit_all_attractions"]) {
			document.getElementById(
				"is-visit-all-" + index.toString() + "-" + model_id.toString()
			).innerHTML = "◯";
		} else {
			document.getElementById(
				"is-visit-all-" + index.toString() + "-" + model_id.toString()
			).innerHTML = "✗";
		}
		document.getElementById(
			"time-visit-all-" + index.toString() + "-" + model_id.toString()
		).innerHTML = res[index]["time"];

		const attractionNameArray = exchangeAttractionNameToNum(
			res[index]["route"]
		);
		const table = document.getElementById(
			"route-" + index.toString() + "-" + model_id.toString()
		);
		attractionNameArray.forEach((attractionName, index) => {
			const newTr = document.createElement("tr");

			const newTdIndex = document.createElement("td");
			const IndexP = document.createElement("p");
			IndexP.textContent = index + 1;
			newTdIndex.appendChild(IndexP);

			const newTdName = document.createElement("td");
			const NameP = document.createElement("p");
			NameP.textContent = attractionName;
			newTdName.appendChild(NameP);

			newTr.appendChild(newTdIndex);
			newTr.appendChild(newTdName);

			table.appendChild(newTr);
		});
	}

	// if (res.status === 200) {
	// 	document.getElementById("date-" + index.toString()).innerHTML = res.date;
	// 	document.getElementById("route-date-" + index.toString()).innerHTML =
	// 		res.date;
	// 	if (res.is_visit_all_attractions) {
	// 		document.getElementById("is-visit-all-" + index.toString() + "-" + model_id.toString()).innerHTML =
	// 			"可";
	// 	} else {
	// 		document.getElementById("is-visit-all-" + index.toString() + "-" + model_id.toString()).innerHTML =
	// 			"不可";
	// 	}
	// 	document.getElementById("time-visit-all-" + index.toString() + "-" + model_id.toString()).innerHTML =
	// 		res.time;
	// 	const attractionNameArray = exchangeAttractionNameToNum(res.route);
	// 	const table = document.getElementById("route-" + index);
	// 	attractionNameArray.forEach((attractionName, index) => {
	// 		const newTr = document.createElement("tr");

	// 		const newTdIndex = document.createElement("td");
	// 		const IndexP = document.createElement("p");
	// 		IndexP.textContent = index + 1;
	// 		newTdIndex.appendChild(IndexP);

	// 		const newTdName = document.createElement("td");
	// 		const NameP = document.createElement("p");
	// 		NameP.textContent = attractionName;
	// 		newTdName.appendChild(NameP);

	// 		newTr.appendChild(newTdIndex);
	// 		newTr.appendChild(newTdName);

	// 		table.appendChild(newTr);
	// 	});
	// } else {
	// 	document.getElementById("date-" + index.toString()).innerHTML = "no data";
	// 	document.getElementById("is-visit-all-" + index.toString()).innerHTML =
	// 		"no data";
	// 	document.getElementById("time-visit-all-" + index.toString()).innerHTML =
	// 		"no data";
	// }
}

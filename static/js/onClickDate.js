function onclickDate(index, model_id) {
	className = "hidden";
	for (let i = 0; i < 7; i++) {
		for (let j = 0; j < 3; j ++) {
			let table = document.getElementById("route-" + i + "-" + j);
			let p = document.getElementById("route-date-" + i + "-" + j);
			console.log(table);
			if (i == index && j == model_id) {
				if (table.classList.contains("hidden")) {
					table.classList.remove("hidden");
				}
				if (p.classList.contains("hidden")) {
					p.classList.remove("hidden");
				}
			} else {
				if (!table.classList.contains("hidden")) {
					table.classList.add("hidden");
				}
				if (!p.classList.contains("hidden")) {
					p.classList.add("hidden");
				}
			}
				
		}
	}
}

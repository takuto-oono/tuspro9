function onclickDate(index) {
	className = "hidden";
	for (let i = 0; i < 7; i++) {
		let table = document.getElementById("route-" + i);
		let p = document.getElementById("route-date-" + i);
		if (i == index) {
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

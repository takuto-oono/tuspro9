function onloadEvent() {
	console.log("onload");
	for (let i = 0; i < 7; i++) {
		getTimeVisitingAllAttractions(i);
	}
}

window.onload = onloadEvent;

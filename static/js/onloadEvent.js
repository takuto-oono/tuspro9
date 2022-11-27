function onloadEvent() {
	console.log("onload");
	// for (let i = 0; i < 7; i++) {
	// 	getTimeVisitingAllAttractions(i);
	// }

	(async () => {
		const p0 = getTimeVisitingAllAttractions(0);
		const p1 = getTimeVisitingAllAttractions(1);
		const p2 = getTimeVisitingAllAttractions(2);
		const p3 = getTimeVisitingAllAttractions(3);
		const p4 = getTimeVisitingAllAttractions(4);
		const p5 = getTimeVisitingAllAttractions(5);
		const p6 = getTimeVisitingAllAttractions(6);
		await Promise.all([p0, p1, p2, p3, p4, p5, p6]);
	})();
	onclickDate(0);
}

window.onload = onloadEvent;

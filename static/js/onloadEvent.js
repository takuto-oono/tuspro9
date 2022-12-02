function onloadEvent() {
	console.log("onload");
	// for (let i = 0; i < 7; i++) {
	// 	getTimeVisitingAllAttractions(i);
	// }

	(async () => {
		const p00 = getTimeVisitingAllAttractions(0, 0);
		const p10 = getTimeVisitingAllAttractions(1, 0);
		const p20 = getTimeVisitingAllAttractions(2, 0);
		const p30 = getTimeVisitingAllAttractions(3, 0);
		const p40 = getTimeVisitingAllAttractions(4, 0);
		const p50 = getTimeVisitingAllAttractions(5, 0);
		const p60 = getTimeVisitingAllAttractions(6, 0);
		const p01 = getTimeVisitingAllAttractions(0, 1);
		const p11 = getTimeVisitingAllAttractions(1, 1);
		const p21 = getTimeVisitingAllAttractions(2, 1);
		const p31 = getTimeVisitingAllAttractions(3, 1);
		const p41 = getTimeVisitingAllAttractions(4, 1);
		const p51 = getTimeVisitingAllAttractions(5, 1);
		const p61 = getTimeVisitingAllAttractions(6, 1);
		const p02 = getTimeVisitingAllAttractions(0, 2);
		const p12 = getTimeVisitingAllAttractions(1, 2);
		const p22 = getTimeVisitingAllAttractions(2, 2);
		const p32 = getTimeVisitingAllAttractions(3, 2);
		const p42 = getTimeVisitingAllAttractions(4, 2);
		const p52 = getTimeVisitingAllAttractions(5, 2);
		const p62 = getTimeVisitingAllAttractions(6, 2);
		await Promise.all([p00, p10, p20, p30, p40, p50, p60, p01, p11, p21, p31, p41, p51, p61, p02, p12, p22, p32, p42, p52, p62]);
	})();


	onclickDate(0);


}

window.onload = onloadEvent;

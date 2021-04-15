var stateObject = {
			"Brand_1": { "Model_1": ["SlType_1", "SlType_2","SlType_3"],
			"Model_2": ["SlType_1", "SlType_2","SlType_3"],
			"Model_3": ["SlType_1", "SlType_2","SlType_3"],
			},
			"Brand_2": { "Model_1": ["SlType_1", "SlType_2","SlType_3"],
			"Model_2": ["SlType_1", "SlType_2","SlType_3"],
			"Model_3": ["SlType_1", "SlType_2","SlType_3"],
			},
			"Brand_3": { "Model_1": ["SlType_1", "SlType_2","SlType_3"],
			"Model_2": ["SlType_1", "SlType_2","SlType_3"],
			"Model_3": ["SlType_1", "SlType_2","SlType_3"],
			},
			}
		
			window.onload = function () {
			var BrandType = document.getElementById("BrandType"),
			ModelType = document.getElementById("ModelType"),
			SlType = document.getElementById("SlType");
			for (var brandtype in stateObject) {
			BrandType.options[BrandType.options.length] = new Option(brandtype, brandtype);
			}
			BrandType.onchange = function () {
			ModelType.length = 1; // remove all options bar first
			SlType.length = 1; // remove all options bar first
			if (this.selectedIndex < 1) return; // done
			for (var modeltype in stateObject[this.value]) {
			ModelType.options[ModelType.options.length] = new Option(modeltype, modeltype);
			}
			}
			BrandType.onchange(); // reset in case page is reloaded
			ModelType.onchange = function () {
			SlType.length = 1; // remove all options bar first
			if (this.selectedIndex < 1) return; // done
			var saletype = stateObject[BrandType.value][this.value];
			for (var i = 0; i < saletype.length; i++) {
			SlType.options[SlType.options.length] = new Option(saletype[i], saletype[i]);
			}
			}




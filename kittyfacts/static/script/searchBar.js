const searchBar = document.getElementById("searchbar");
            const searchResult = document.getElementById("searchResult");

            function addSearchResult(text , link){
                const divNode = document.createElement("div");
                divNode.className = "resultAnchor"
                const anchorNode = document.createElement("a");
                anchorNode.href = link
                anchorNode.className = "link-dark text-decoration-none font-bolder fs-5"
                const textNode = document.createTextNode(text);
                anchorNode.appendChild(textNode)
                divNode.appendChild(anchorNode)
                searchResult.appendChild(divNode)
            }
            searchBar.addEventListener("input", function() {
            searchResult.innerHTML = ''
            const query = this.value;

            axios.get(`http://127.0.0.1:8000/fact?title=${query}`)
                .then(function(response) {
                    for (fact of response.data){
                        addSearchResult(fact['title'] , "http://127.0.0.1:8000/fact/" + fact["title"])
                    }
                })
                .catch(function(error) {
                    console.error('Error fetching data:', error);
                    const noResult = document.createElement("h3")
                    const text = document.createTextNode("No Results")
                    noResult.appendChild(text)
                    searchResult.appendChild(noResult)
                });
            });

            searchResult.addEventListener("click", function(e) {
                const clickedAnchor = e.target.closest(".resultAnchor");
                if (clickedAnchor) {
                    const anchorLink = clickedAnchor.querySelector("a").href;
                    window.location.href = anchorLink;
                }
            });
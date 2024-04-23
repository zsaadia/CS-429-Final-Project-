# CS-429-Final-Project-

<h2> Abstract </h2>
    <p> This project puts forth the development of an information retrieval and search system. This system consists of a web document crawler, an indexer, and a query processor. It utilizes Python 3.10+ along with Scrapy 2.11+, Scikit-Learn 1.2+, and Flask 2.2+.  The web crawler assembled using Scrapy retrieves web documents using seed URLs. The indexer implemented with Scikit-Learn creates an inverted index using TF-IDF scores and cosine similarities. The processor, made using Flask, handles text queries and returns top-K ranked results. </p>
    <p>The objective for this project was to imitate and create a smaller scale version of a web document retrieval system and implement all the knowledge acquired over the course of the semester about IR. The design of this system emphasizes ease and a base level implementation. </p>
    <p>Next steps for this project would be to advance the different components with a deeper understanding and further research. Specifically, the crawler could be further developed to implement concurrent and distributed crawling. The indexer would potentially use vector embedding representation and semantic search using kNN similarity. The processor would integrate additional features such as query spelling-correction and expansion. Next steps would also include evaluation of the system’s performance on large-scale datasets. <br  /> <br  />In the end, this basic implementation paves way for a robust web document retrieval system and knowledge surfing. 
</p>


<h2> Overview </h2>
<p>This project consists of three main parts: the crawler, indexer, and processor</p>
   
<p>Relevant Literature:</p>
        <p>This project draws knowledge and concpets mainly from the textbook <em>Introduction to Information Retrieval</em> by Chirstopher D Manning, Prabhakar Raghavan and Hinrich Schutze. The book offers a breakdown of information retrieval using a modern apprach from a computer science perspective.</p>
        <p> This project touches topics covered in the textbook such as: index construction, scoring, term weighting and the vector space model, computing cosine similarity scores, and ranked retrieval.  </p>
<h2> Design </h2>
    <ol>
        <li><strong>Web Document Crawler:</strong><ul>
            <p>Implemented using Scrapy, the crawler basically accesses and retrieves web documents using seed URL, while specifying max pages and depth.</p>
            </ul></li>
        <li><strong>Indexer:</strong><ul>
            <p>The indexer is built using Scikit-Learn where it outputs an inverted index of TF-IDF weight representation and cosine similarities.</p></ul></li>
        <li><strong>Query Processor:</strong><ul>
            <p>The processor was built using Flask, to process queries in json format, sorting based on similarity scores and returning the top-K ranked results based on the indexed documents.</p></ul></li>
    </ol> 
    <p>Each document operates independently, which enables flexibity and scalability in the management of the system.</p>

<h2> Architecture </h2>
    <p>The crawler component utilizes Scrapy, a high-level web crawling and scraping framwework in python that extracts data from the web. We use scrapy to implement a local scrawler.</p>
    <p>The indexer utilizes the python library Scikit-Learn also known as sklearn. It allows for classification and retrieval of query terms and creation of an inverted index.</p>
    <p>The query processor is Flask based which provides a small scalable web server for handling user queries.  </p>
<h2> Operation </h2>

<h2> Conclusion </h2>

<h2> Test Cases </h2>

<h2> Source Code </h2>

<h2> Bibliography </h2>
    <p>Chatgpt. Accessed April 23, 2024. https://chat.openai.com. </p>
    <p>Manning, Christopher D., Prabhakar Raghavan, and Hinrich Schütze. <em>An introduction to information retrieval.</em> Cambridge: Cambridge University Press, 2022.  </p>
    <p>“Scikit-Learn.” scikit. Accessed April 22, 2024. https://scikit-learn.org/stable/. </p>
    <p>“Scrapy 2.11 Documentation.” Scrapy 2.11 documentation - Scrapy 2.11.1 documentation, April 11, 2024. https://docs.scrapy.org/en/latest/. </p>
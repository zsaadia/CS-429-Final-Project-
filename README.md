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
    <p>The operation of the system requires the user to interact and start the individual components and make sure they have Python 3.10+ and the respective proper softwares and libraries.</p>
    <p>For the crawler, the user needs to make sure they have scrpy installed which can easily be done through pip and have a spider running. The inputs here are the seed URLs and the specifications for the pages and depth.  </p>
    <p>For the indexer, the user needs to make sure the scikit-learn python package is installed. It does not require manual execution because the indexer is given the queries. </p>
    <p>For the processor, the user needs to have flask installed. To operate the processor, first run the processor file, then the command <code>python3 test_processor.py </code> for Mac or linux or <code> py -3 test_processor.py</code> for Windows. </p>
<h2> Conclusion </h2>
    <p>The system was successful in creating a comprehensive solution for web document retrieval. Each component perfroms their unique capabilities and successfully prints results. It demonstrates the use of open-source Python libraries and frameworks.</p>

<h2>Data Sources</h2>
    <p>No external data sources were used expect in the crawler for the seed URLs which used wikipedia pages and a quotes website. </p>

<h2> Test Cases </h2>
    <p> For the crawler, the test cases are provided in crawler_test.py which have three different URLs for the program to crawl.</p>
    <p>For the indexer, the test case that was provided in the indexer program has been copied to its own file named indexer_test to make it easier to see and understand.</p>
    <p>The processor also has its own test file named test_processor that is used to run the code and display the output.</p>
<h2> Source Code </h2>
    <p> For this project the source code was produced by ChatGPT.   </p>

<h2> Bibliography </h2>
    <p>Chatgpt. Accessed April 23, 2024. https://chat.openai.com. </p>
    <p>Manning, Christopher D., Prabhakar Raghavan, and Hinrich Schütze. <em>An introduction to information retrieval.</em> Cambridge: Cambridge University Press, 2022.  </p>
    <p>“Scikit-Learn.” scikit. Accessed April 22, 2024. https://scikit-learn.org/stable/. </p>
    <p>“Scrapy 2.11 Documentation.” Scrapy 2.11 documentation - Scrapy 2.11.1 documentation, April 11, 2024. https://docs.scrapy.org/en/latest/. </p>
#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
#나는 빈집으로 가고 있습니다.     //나는 반장으로 뽑혔습니다.     //나는 이불로 침대를 덮었습니다.
print("Content-Type: text/html; charset=utf-8")
print()

import cgi
form = cgi.FieldStorage()
sentence = form['sentence'].value
window = form['window'].value
windowSize = window.replace("window","")


print('''<!doctype html>
<html>
<head>
  <title>Function recognition</title>
  <meta charset="utf-8">
</head>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<link href="System.css" rel="stylesheet">
<link href="loding.css" rel="stylesheet">
<body>

<header>
      <div class="collapse bg-dark" id="navbarHeader">
        <div class="container">
          <div class="row">
            <div class="col-sm-8 col-md-7 py-4">
              <h4 class="text-white">About</h4>
                <p class="text-muted">Intended construal of a polysemous word occurs within a range of words, delivering various frame-semantic meanings (Goldberg,2006) and yet purport similar interpretations (Harris,1954). In this regard, context window-a range of words surrounding a target word, affecting the determination of its characteristics-is drawing attention to the computational understanding of combinatorial properties of words.
                <br><br>
                We ask how context window addresses polysemy interpretation in Korean, a language typologically different from the major Indo-European languages investigated for this task. We report computational simulations that explore how various sizes of context window account for polysemy of -(u)lo, which manifests polysemy due to its multiple functions mapped onto one form. For this purpose, we used the Sejong corpus, with semantic annotations involving this postposition cross-verified by three native speakers of Korean (<i>κ</i>=0.95). Employing a distributional semantic model, we devised an unsupervised learning algorithm by combining Singular Value Decomposition with Positive Pointwise Mutual Information. Using cosine similarity scores between -(u)lo and its co-occurring content words, dubbed the similarity-based estimate (Dagan et al, 1993), model performance was measured through accuracy rates that the model classiﬁed test sentences by the functions of -(u)lo, with manipulation of context window size from one to ten.
                <br><br>
                Our model achieved the highest classiﬁcation accuracy rate in the window size of one, and the accuracy rates decreased as the window size increased. This trend aligns with advantages of small window sizes (Bullinaria&Levy,2007). Considering that a narrower range of context window relates more to syntactic than to sematic information (Patel et al.,1997), our model may have employed structural, rather than semantic, characteristics of tri-grams (word-target-word) for the best classiﬁcation performance. Given the networks of interlinked clusters of words and symbolic units in human cognition (<i>construct-i-con</i>; Goldberg,2006), our findings throw light on relations between a polysemous word and an abstract schema including the word, represented as context window, in addressing word-level polysemy.
                <br><br>
                <strong style="color:white">References</strong><br>
                <ul>
                <li class="text-muted">Bullinaria, John A & Joseph P. Levy. 2007. Extracting semantic representations from word co- occurrence statistics: A computational study. Behavior Research Methods 39(3). 510–526.</li>
                <li class="text-muted">Goldberg, A. E. 2006 Constructions at work: The nature of generalization in language. Oxford: Oxford University Press.</li>
                <li class="text-muted">Harris, Zellig S. 1954 Distributional Structure. WORD. 10(2-3). 146-162.</li>
                <li class="text-muted">Ido Dagan, Shaul Marcus, & Shaul Markovitch. 1993. Contextual word similarity and estimation from sparse data. In Proceedings of ACL-93, 164-171.</li>
                <li class="text-muted">Malti Patel, John A. Bullinaria, & Joseph P. Levy. 1997. Extracting semantic representations from large text corpora. In 4th Neural Computation and Psychology Workshop, London, 9–11 April 1997, 199–212.</li>
                </ul></p>
            </div>
            <div class="col-sm-4 offset-md-1 py-4">
              <h4 class="text-white">Contact</h4>
              <ul class="list-unstyled">
                <li><a href="https://seongmin-mun.github.io/MyWebsite/Seongmin/index.html" class="text-white">Seongmin Mun</a></li>
                <li><a href="https://gyuhoshin.weebly.com/" class="text-white">Gyu-ho Shin</a></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <div class="navbar navbar-dark bg-dark box-shadow">
        <div class="container d-flex justify-content-between">
          <a href="#" class="navbar-brand d-flex align-items-center">
            <strong>IMPRS poster: Context window size and polysemy interpretation: A case of Korean adverbial postposition <i>-(u)lo</i></strong>
          </a>
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarHeader" aria-controls="navbarHeader" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
        </div>
      </div>
    </header>
    <main role="main">

        <div class="container">
          <br>
          <h1 class="jumbotron-heading"><a href="index.py">Similarity Based Estimation: -(u)lo</a></h1><br>
          <form name="frm" action="result.py" method="post">
          <h4 class="jumbotron-heading"><p>Context window size</p></h4>

                <select id="op_window" name="window">
                    <option value="window1" selected="selected">window 1</option>
                    <option value="window2">window 2</option>
                    <option value="window3">window 3</option>
                    <option value="window4">window 4</option>
                    <option value="window5">window 5</option>
                    <option value="window6">window 6</option>
                    <option value="window7">window 7</option>
                    <option value="window8">window 8</option>
                    <option value="window9">window 9</option>
                    <option value="window10">window 10</option>
                </select>
                <br><br><h4 class="jumbotron-heading"><p>Input Sentence</p></h4>
                <div class="form-group shadow-textarea">
              <p><textarea class="form-control z-depth-1" id="exampleFormControlTextarea6" cols = "100" rows="10" name="sentence" placeholder="Input your sentence ..." style="background:#fafbfc">{sentence}</textarea></p>
              </div>
              <p><input type="submit" class="btn btn-primary my-2" style="float: right;" value="Analyze"></p>
          </form>
          <br><br>
          <div class="loading-container">
            <div class="loading"></div>
            <div id="loading-text">loading</div>
        </div>
    </main>

  <script>
    $('#op_window option[value={window}]').prop('selected', 'selected').change();
    document.frm.submit()
  </script>


</body>
</html>
'''.format(sentence=sentence, window=window))

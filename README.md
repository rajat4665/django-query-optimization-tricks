<!-- wp:image {"sizeSlug":"large"} -->
<figure class="wp-block-image size-large"><img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&amp;ixlib=rb-1.2.1&amp;auto=format&amp;fit=crop&amp;w=1050&amp;q=80" alt=""/></figure>
<!-- /wp:image -->

<!-- wp:heading -->
<h2>Introduction:</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Hi readers, I hope you guys are doing good and safe, Today i came up with new topic of Django framework. As i wrote many i article on Django framework , well if you are new you can see my previous post about Django framework. This framework written in python language and its very secure even some famous websites such as Instagram, Reddit and even Nasa's website itself developed in this framework because it comes with a lot of per-build features such as Admin pannel, ORM queryset and generic methods which save lot of time and make web development process extremely fast. But when we develop a web app which have large database and thousands of daily visitors . So in that cases database queries optimization is like a oxygen, if don't your web server can't handle this much load and eventually down. For tackling these kind of problems optimization act as a lifesaver. </p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p> </p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3>Requirements:</h3>
<!-- /wp:heading -->

<!-- wp:list -->
<ul><li>Python 3</li><li>Django 2.2</li><li>Django rest framework</li><li>Django debug toolbar</li></ul>
<!-- /wp:list -->

<!-- wp:heading -->
<h2>what you will learn from this tutorial:</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul><li>rest API development with Django rest frame work</li><li>optimizing database queries using select_related and prefetch_related</li><li>play with Django Queryset </li><li>Using Django generic methods</li></ul>
<!-- /wp:list -->

<!-- wp:heading -->
<h2>Database structure</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>For this implementation i used SQLite relational database, Which have three tables  Publisher, Book, Store each of them is related using Foreign key and many to many relation.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>As you can see in the bellow image Store table is connected with book table using many to many relationship and Book table further connected with Publisher using foreignkey  (one to many relation ship).</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>I pre populated database for this query optimization testing, I user faker module to insert fake data. you guys can view this database's data by its <strong>admin pane  </strong>or you guys can view this db.slite3 file using sql browser.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>admin panel link => 127.0.0.1:8000/admin/</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>username = admin</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>password = admin</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":230,"width":840,"height":581,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large is-resized"><img src="https://getpython.files.wordpress.com/2021/07/screenshot-from-2021-07-08-23-06-33.png?w=1024" alt="" class="wp-image-230" width="840" height="581"/></figure>
<!-- /wp:image -->

<!-- wp:heading -->
<h2>how to run this code:</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul><li>clone or download it from <a rel="noreferrer noopener" href="https://github.com/rajat4665/django-query-optimization-tricks" data-type="URL" data-id="https://github.com/rajat4665/django-query-optimization-tricks" target="_blank">my github rep</a><a href="https://github.com/rajat4665/django-query-optimization-tricks" data-type="URL" data-id="https://github.com/rajat4665/django-query-optimization-tricks" target="_blank" rel="noreferrer noopener">o</a></li><li>install requirements.txt file using this cmd <em>(<strong>pip3 install requirements.txt</strong></em> )</li><li>run this project using this cmd (<em><strong>python3 manage.py runserve</strong></em>r )</li></ul>
<!-- /wp:list -->

<!-- wp:heading -->
<h2>With and without optimization:</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":232,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://getpython.files.wordpress.com/2021/07/screenshot-from-2021-07-08-23-13-29.png?w=1024" alt="" class="wp-image-232"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>As you guys can see I have created two classes here one is normal StoreList which render data without and optimization and another class named as OptimizedStoreList where I used prefetch_related and select_related methods for obtaining data without any database query.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For viewing number of queries i used Django debug toolbar , which is Django profiler, it depicts us various details such as number of database queries, computation time, cache and signal requests for specific page. Sounds interesting ? you guys can explore it from <a rel="noreferrer noopener" href="https://django-debug-toolbar.readthedocs.io/en/latest/" data-type="URL" data-id="https://django-debug-toolbar.readthedocs.io/en/latest/" target="_blank"> official docs</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>select_related and prefetch_related queryset's methods which allow us to take relational db data in a same query.<br>-- for ForeignKey relationship we use select_related method<br>-- for ManyToManyField relationship we use prefetch_related method</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For StoreList with this default query set it shows <strong><em>185 databases queries which take 55.45ms</em></strong> time in my local system.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":234,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://getpython.files.wordpress.com/2021/07/screenshot-from-2021-07-08-23-26-07.png?w=1024" alt="" class="wp-image-234"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For OptimizedStoreList, here I used select related and prefetch related and the number of database queries reduced to 5 from 185.</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":235,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://getpython.files.wordpress.com/2021/07/screenshot-from-2021-07-08-23-28-05.png?w=1024" alt="" class="wp-image-235"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>Conclusion:</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>If you guys developing big application and big database spend your time on query optimization it is totally worth it and it will improve your app speed and reduce computation cost. </p>
<!-- /wp:paragraph -->

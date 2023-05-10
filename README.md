   Список команд, запускаемых в Django shell

        1. Создать двух пользователей (с помощью метода User.objects.create_user('username')) 
           
            from MainTable.models import *
            user1 = User.objects.create_user('Pyt')
            user2 = User.objects.create_user('Hon')
		
        2. Создать два объекта модели Author, связанные с пользователями.
           
            Author.objects.create(user = user1)
            Author.objects.create(user = user2)
           

        3. Добавить 4 категории в модель Category.
           
           Category.objects.create(name = 'Hot')
           Category.objects.create(name = 'Cars')
           Category.objects.create(name = 'Crypto')
           Category.objects.create(name = 'Humor')
            
        4. Добавить 2 статьи и 1 новость.
           
           Post.objects.create(type_paper='ART', title='Kaspa to the moon', text_post='It`s a very long story', author=author1)
           Post.objects.create(type_paper='ART', title='Honda present a new Civic!', text_post='It`s a very long story', author=author2)
           Post.objects.create(type_paper='NWS', title='Kolobok hanged himself', text_post='It`s a very long story', author=author1)
           
            
        5. Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
           
           Post.objects.get(id=1).connect_categories.add(Category.objects.get(id=3))
           Post.objects.get(id=1).connect_categories.add(Category.objects.get(id=1))
           Post.objects.get(id=2).connect_categories.add(Category.objects.get(id=2))
           Post.objects.get(id=3).connect_categories.add(Category.objects.get(id=4))
            
        6. Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
           
            Comment.objects.create(text_comment='To the mooooooon!!!', comment_post=Post.objects.get(id=1), comment_user=user1)
           Comment.objects.create(text_comment='Let`s goooo!', comment_post=Post.objects.get(id=1), comment_user=user2)
           Comment.objects.create(text_comment='Cool', comment_post=Post.objects.get(id=2), comment_user=user1)
           Comment.objects.create(text_comment='lol', comment_post=Post.objects.get(id=3), comment_user=user2)
            
        7. Применяя функции like() и dislike()к статьям/новостям и комментариям, скорректировать рейтинги этих объектов. 
           
           Comment.objects.get(id=1).like()
           Comment.objects.get(id=2).like()
           Comment.objects.get(id=3).like()
           Comment.objects.get(id=4).like()
           Comment.objects.get(id=1).dislike()
           Comment.objects.get(id=2).dislike()
           Comment.objects.get(id=3).dislike()
           Comment.objects.get(id=4).dislike()
           Post.objects.get(id=1).like()
           Post.objects.get(id=1).dislike()
           Post.objects.get(id=2).like()
           Post.objects.get(id=2).dislike()
           Post.objects.get(id=3).like()
           Post.objects.get(id=3).dislike()
           
        8. Обновить рейтинги пользователей.
           
           update1 = Author.objects.get(id=1)
           update1.update_rating()
           update1.user_rating
           update2 = Author.objects.get(id=2)
           update2.update_rating()
           update2.user_rating
           
        9. Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
           
            best = Author.objects.all().order_by('-user_rating').values('user', 'user_rating')[0]
           print(best)
           
        10. Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.

           Post.objects.all().order_by().values('time_in', 'author__user__username','rating_post', 'title', 'text_post')[0]
            
        11. Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
           Comment.objects.all().order_by().values('time_comment', 'comment_user__username', 'comment_post', 'rating_comment', 'text_comment')[0]

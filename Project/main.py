class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"Title: {self.title}\nContent: {self.content}\nAuthor: {self.author}\n"


class Blog:
    def __init__(self, name):
        self.name = name
        self.posts = []

    def add_post(self, title, content, author):
        new_post = Post(title, content, author)
        self.posts.append(new_post)
        print(f"Post '{title}' added successfully!")

    def list_all_posts(self):
        if not self.posts:
            print("No posts available.")
        else:
            for post in self.posts:
                print(post)

    def list_posts_by_author(self, author):
        posts_by_author = [post for post in self.posts if post.author == author]
        if not posts_by_author:
            print(f"No posts found by author '{author}'.")
        else:
            for post in posts_by_author:
                print(post)

    def delete_post(self, title):
        for post in self.posts:
            if post.title == title:
                self.posts.remove(post)
                print(f"Post '{title}' deleted successfully!")
                return
        print(f"Post '{title}' not found.")

    def edit_post(self, title, new_title=None, new_content=None, new_author=None):
        for post in self.posts:
            if post.title == title:
                new_title = input("Enter new title (leave blank to keep current): ")
                new_content = input("Enter new content (leave blank to keep current): ")
                new_author = input("Enter new author (leave blank to keep current): ")
                my_blog.edit_post(title, new_title or None, new_content or None, new_author or None)

                if new_title:
                    post.title = new_title
                if new_content:
                    post.content = new_content
                if new_author:
                    post.author = new_author
                print(f"Post '{title}' updated successfully!")
                return
        print(f"Post '{title}' not found.")

    def display_latest_posts(self, count=3):
        latest_posts = self.posts[-count:]
        if not latest_posts:
            print("No posts available.")
        else:
            for post in latest_posts:
                print(post)


def print_menu():
    print("\nBlog Management Menu:")
    print("1. Add a post")
    print("2. List all posts")
    print("3. List posts by author")
    print("4. Delete a post")
    print("5. Edit a post")
    print("6. Display latest posts")
    print("7. Exit")


def main():
    my_blog = Blog("My Awesome Blog")

    while True:
        print_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author name: ")
            my_blog.add_post(title, content, author)

        elif choice == "2":
            my_blog.list_all_posts()

        elif choice == "3":
            author = input("Enter author name: ")
            my_blog.list_posts_by_author(author)

        elif choice == "4":
            title = input("Enter the title of the post to delete: ")
            my_blog.delete_post(title)

        elif choice == "5":
            title = input("Enter the title of the post to edit: ")
            

        elif choice == "6":
            count = int(input("Enter the number of latest posts to display: "))
            my_blog.display_latest_posts(count)

        elif choice == "7":
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
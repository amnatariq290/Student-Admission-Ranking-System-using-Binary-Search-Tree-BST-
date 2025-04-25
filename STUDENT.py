import random

class StudentNode:
    def __init__(self, name, app_id, score):
        self.name = name
        self.app_id = app_id
        self.score = score
        self.left = None
        self.right = None

class StudentBST:
    def __init__(self):
        self.root = None

    def insert(self, root, student):
        if root is None:
            return student
        if student.score < root.score:
            root.left = self.insert(root.left, student)
        elif student.score > root.score:
            root.right = self.insert(root.right, student)
        else:
            print(f"Duplicate score not allowed for {student.name}.")
        return root

    def in_order(self, root):
        if root:
            self.in_order(root.left)
            print(f"{root.name} (ID: {root.app_id}, Score: {root.score})")
            self.in_order(root.right)

    def search(self, root, score):
        if root is None or root.score == score:
            return root
        if score < root.score:
            return self.search(root.left, score)
        return self.search(root.right, score)

    def print_range(self, root, x, y):
        if root is None:
            return
        if x < root.score:
            self.print_range(root.left, x, y)
        if x <= root.score <= y:
            print(f"{root.name} (ID: {root.app_id}, Score: {root.score})")
        if root.score < y:
            self.print_range(root.right, x, y)

    def print_rank(self, root, score):
        return self._count_less_than(root, score)

    def _count_less_than(self, root, score):
        if root is None:
            return 0
        if root.score < score:
            return 1 + self._count_less_than(root.left, score) + self._count_less_than(root.right, score)
        return self._count_less_than(root.left, score)

# Sample student names provided by user
names = ["Saira", "Amna", "Khadija", "Ahmad", "Shayan", "Zainab", "Hina", "Tehman", "Yahya", "Affan", "Ali Sher", "Bareera", "Hunzala", "Abeera", "Aryash"]
scores = random.sample(range(60, 100), len(names))  # unique scores between 60-99

bst = StudentBST()
root = None

# Insert students
for i, name in enumerate(names):
    student = StudentNode(name, f"APP{i+1:03d}", scores[i])
    root = bst.insert(root, student)

# Menu interface
def menu():
    while True:
        print("\n===== Student Admission Ranking System =====")
        print("1. Display All Students (In-order Traversal)")
        print("2. Search Student by Score")
        print("3. Print Students Within Score Range")
        print("4. Print Rank of a Student (How many scored less)")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            bst.in_order(root)
        elif choice == '2':
            s = int(input("Enter score to search: "))
            result = bst.search(root, s)
            if result:
                print(f"Found: {result.name} (ID: {result.app_id}, Score: {result.score})")
            else:
                print("Student not found.")
        elif choice == '3':
            x = int(input("Enter lower bound score: "))
            y = int(input("Enter upper bound score: "))
            bst.print_range(root, x, y)
        elif choice == '4':
            s = int(input("Enter student score to check rank: "))
            print(f"Number of students with score less than {s}: {bst.print_rank(root, s)}")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")

# Run menu
menu()

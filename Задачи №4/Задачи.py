#Zadacha 1

from abc import ABC, abstractmethod

def get_col(lst: list[list[any]], col: int) -> list[any]:
    col_lst = [row[col] for row in lst]

    return col_lst

# lst = [[1, 2, 3], ["One", "Two", "Three"], [1.00, 2.00, 3.00]]
#print(f"{get_col(lst, 1) = }")

#Zadacha 2

class ArithmeticOperation(ABC):

    @abstractmethod
    def arithmetic_op(self, el1, el2):
        pass

    def apply(self, lst1: list[float], lst2: list[float]) -> list[float]:
        lst_res = []
        lst_longer = lst1 if len(lst1) > len(lst2) else lst2
        lst_shorter = lst2 if len(lst1) > len(lst2) else lst1

        for i in range(len(lst_longer)):
            el_longer = lst_longer[i]
            el_shorter = lst_shorter[i] if i < len(lst_shorter) else None

            if el_shorter is not None:
                el_longer = self.arithmetic_op(el_longer, el_shorter)

            lst_res.append(el_longer)

        return lst_res
        

class Add(ArithmeticOperation):

    def arithmetic_op(self, el1, el2):
        return el1 + el2

class Subtract(ArithmeticOperation):

    def arithmetic_op(self, el1, el2):
        return el1 - el2

class Multiply(ArithmeticOperation):

    def arithmetic_op(self, el1, el2):
        return el1 * el2

class Divide(ArithmeticOperation):

    def arithmetic_op(self, el1, el2):
        return el1 / el2
        

def apply_arithmetic_operations(actions: list[ArithmeticOperation], items: list[list[float]]) -> list[float]:
    
    if len(items) == 0:
        return items
    
    last_result = items[0]

    for i in range(1, len(items)):

        if not i - 1 < len(actions):
            return last_result

        next_list = items[i]
        next_action = actions[i - 1]

        last_result = next_action.apply(last_result, next_list)

    return last_result

# some_arithmetic_op = ArithmeticOperation()
add_op = Add()

print(add_op.apply([1, 2, 3], [4, 5, 6, 7])) #[5, 7, 9, 7]
print(add_op.apply([4, 5, 6, 7], [1, 2, 3])) #[5, 7, 9, 7]
print(add_op.apply([4, 5, 6, 7], [])) #[4, 5, 6, 7]
print(add_op.apply([], [])) #[]
print(add_op.apply([], [1])) #[1]
print(add_op.apply([1], [2, 3])) #[3, 3]
print(add_op.apply([3, 3], [4, 5, 6])) #[7, 8, 6]

print()

#Add
print(apply_arithmetic_operations(
    [Add(), Add(), Add()],
    [[], [1], [2, 3], [4, 5, 6]])) #[7, 8, 6]
print(apply_arithmetic_operations(
    [],
    [[], [1], [2, 3], [4, 5, 6]])) #[]

print(apply_arithmetic_operations(
    [Add(), Add()],
    [[], [1], [2, 3], [4, 5, 6]])) #[3, 3]

print(apply_arithmetic_operations(
    [Add(), Add(), Add(), Add()],
    [[], [1], [2, 3], [4, 5, 6]])) #[7, 8, 6]

print(apply_arithmetic_operations(
    [Add(), Add(), Add(), Add()],
    [[]])) #[]

print(apply_arithmetic_operations(
    [],
    [[]])) #[]


#Multiply
print(apply_arithmetic_operations(
    [Multiply(), Multiply(), Multiply()],
    [[], [1], [2, 3], [4, 5, 6]])) #[8, 15, 6]
print(apply_arithmetic_operations(
    [],
    [[], [1], [2, 3], [4, 5, 6]])) #[]

print(apply_arithmetic_operations(
    [Multiply(), Multiply()],
    [[], [1], [2, 3], [4, 5, 6]])) #[2, 3]

print(apply_arithmetic_operations(
    [Multiply(), Multiply(), Multiply(), Multiply()],
    [[], [1], [2, 3], [4, 5, 6]])) #[8, 15, 6]

print(apply_arithmetic_operations(
    [Multiply(), Multiply(), Multiply(), Multiply()],
    [[]])) #[]

print(apply_arithmetic_operations(
    [],
    [[]])) #[]


        


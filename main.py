import parser
import task2


def parse_command():
    user_input = input('> ').split(maxsplit=1)

    while len(user_input) == 0:
        user_input = input('> ').split(maxsplit=1)

    command = user_input[0]
    arguments = ''

    if len(user_input) > 1:
        arguments = user_input[1]

    return command, arguments


def ask_save_container(storage: task2.Container):
    answer = input('Do you want to save container?(y/n): ')

    if answer == 'y':
        storage.save()


def greeting(username: str):
    print(f'>>>>>>>>>> Hello, {username}!')


def exec_command(command: str, arguments: str, storage: task2.Container) -> bool:
    match command:

        case 'exit':
            answer = input('Do you want to save container?(y/n): ')

            if answer == 'y':
                storage.save()
                print('>>>>>>>>>> Container was saved successfully!')

            return False

        case 'add':
            arguments_list = arguments.split()

            for el in arguments_list:
                storage.add(el)

            print('>>>>>>>>>> added!')

        case 'remove':
            storage.remove(arguments)
            print('>>>>>>>>>> removed!')

        case 'list':
            storage.list()

        case 'find':

            if len(arguments) != 0:
                arguments_list = arguments.split()

                for el in arguments_list:
                    found = storage.find(el)
                    print(f'>>>>>>>>>> {el} found' if found else f'{el} not found')

        case 'grep':
            res = storage.grep(arguments)

            if len(res) != 0:
                print('>>>>>>>>>> Found values: ' + str(res))

        case 'save':
            storage.save()
            print('>>>>>>>>>> Container was saved successfully!')

        case 'help':
            print(task2.FUNCTIONS)

        case 'switch':
            ask_save_container(storage)
            storage.switch(arguments)
            greeting(arguments)
    return True


def task1():
    text = input('Input text: ').lower()
    print('Amount of sentences: ', parser.count_sentences(text))
    print('Amount of non-declarative sentences: ', parser.count_non_declarative_sentences(text))
    print('Average sentence length: ', parser.average_sentence_length(text))
    print('Average word length: ', parser.average_word_length(text))
    print('Top k repeated anagrams: ', parser.top_k_repeated_n_grams(text))


def task2():
    print('>>>>>>>>>> Welcome to storage for unique elements.')
    username = input('>>>>>>>>>> Please, introduce yourself: ')
    storage = task2.Container(username)
    print(f'>>>>>>>>>> Hello, {username}!')
    print('>>>>>>>>>> Type \'help\' to check list of commands.')
    run = True

    while run:
        command, args = parse_command()
        run = exec_command(command, args, storage)


def main():
    task = input(print('Please, choose the task (1/2).'))

    if task == 1:
        task1()

    if task == 2:
        task2()


if __name__ == "__main__":
    main()

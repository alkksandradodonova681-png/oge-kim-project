import argparse
import os
from loader import Loader
from validator import Validator
from generate import Generator
from exporter import Exporter

def main():
    parser = argparse.ArgumentParser(description="Генератор КИМ ОГЭ")
    parser.add_argument("--subject", default="math", help="Предмет (math или phys)")
    parser.add_argument("--count", type=int, default=1, help="Количество вариантов")
    args = parser.parse_args()

    print(f"Загрузка данных для {args.subject}...")
    loader = Loader()
    plan = loader.load_plan(args.subject)
    bank = loader.load_bank(args.subject)

    print("Валидация данных...")
    validator = Validator(plan, bank)
    is_valid, errors = validator.validate()
    if not is_valid:
        print("ОШИБКИ ВАЛИДАЦИИ:")
        for err in errors:
            print(f" - {err}")
        return

    print("Генерация вариантов...")
    gen = Generator(plan, bank)
    exporter = Exporter()

    # Создаем папку output, если её нет
    output_dir = f"output/{args.subject}"
    os.makedirs(output_dir, exist_ok=True)

    for i in range(1, args.count + 1):
        variant = gen.generate_variant(i)
        output_file = os.path.join(output_dir, f"variant_{i}.docx")
        exporter.export_to_docx(variant, output_file)

    print("Готово!")

if __name__ == "__main__":
    main()
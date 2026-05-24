class ForwardChaining:
    def __init__(self, rules, facts):
        self.rules = rules
        self.facts = set(facts)

    def apply_rules(self):
        while True:
            new_facts = set()

            for antecedent, consequent in self.rules:
                if antecedent.issubset(self.facts):
                    new_facts.add(consequent)

            if not new_facts.difference(self.facts):
                break

            self.facts.update(new_facts)

    def get_facts(self):
        return self.facts


# Define rules as (antecedent, consequent) pairs
rules = [
    ({"has_fur(tiger)"}, "mammal(tiger)"),
    ({"has_feathers(penguin)", "lays_eggs(penguin)"}, "bird(penguin)"),
    ({"lays_eggs(sparrow)", "has_feathers(sparrow)"}, "bird(sparrow)"),
    ({"has_fur(cat)"}, "mammal(cat)"),
]

# Initial facts
initial_facts = [
    "has_fur(tiger)",
    "has_feathers(penguin)",
    "lays_eggs(penguin)",
    "lays_eggs(sparrow)",
    "has_fur(cat)",
]

fc = ForwardChaining(rules, initial_facts)

fc.apply_rules()

print("Derived Facts:", fc.get_facts())


class BackwardChaining:
    def __init__(self, rules, facts):
        self.rules = rules
        self.facts = set(facts)

    def is_fact(self, fact):
        if fact in self.facts:
            return True

        for ant, cons in self.rules:
            if cons == fact and all(self.is_fact(a) for a in ant):
                return True
        return False


rules = [
    ({"has_fur(tiger)"}, "mammal(tiger)"),
    ({"has_feathers(penguin)", "lays_eggs(penguin)"}, "bird(penguin)"),
    ({"lays_eggs(sparrow)", "has_feathers(sparrow)"}, "bird(sparrow)"),
    ({"has_fur(cat)"}, "mammal(cat)"),
]

facts = {
    "has_fur(tiger)",
    "has_feathers(penguin)",
    "lays_eggs(penguin)",
    "lays_eggs(sparrow)",
    "has_fur(cat)",
}

goals = ["mammal(tiger)", "bird(penguin)", "bird(sparrow)", "mammal(cat)"]

bc = BackwardChaining(rules, facts)

for g in goals:
    print(f"Goal {g} {'can' if bc.is_fact(g) else 'cannot'} be derived from the facts.")

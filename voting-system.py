class VotingSystem:
    def __init__(self):
        self.voted_registry = {}
        self.candidate_votes = {}
    
    def vote(self, voter_id: str, candidate: str) -> str:
        if voter_id in self.voted_registry:
            return "Erro: Eleitor já votou."
        
        self.voted_registry[voter_id] = True
        
        if candidate in self.candidate_votes:
            self.candidate_votes[candidate] += 1
        else:
            self.candidate_votes[candidate] = 1
        
        return f"Voto registrado para {candidate}!"
    
    def show_results(self) -> dict:
        if not self.candidate_votes:
            return "Nenhum voto registrado ainda."
        
        sorted_results = dict(sorted(
            self.candidate_votes.items(),
            key=lambda x: x[1],
            reverse=True
        ))
        
        return sorted_results
    
    def get_total_voters(self) -> int:
        return len(self.voted_registry)


def main():
    voting_system = VotingSystem()
    
    print(voting_system.vote("123", "Alice"))
    print(voting_system.vote("456", "Bob"))
    print(voting_system.vote("789", "Alice"))
    
    print(voting_system.vote("123", "Bob"))
    
    print("\nResultados da eleição:")
    results = voting_system.show_results()
    for candidate, votes in results.items():
        print(f"{candidate}: {votes} votos")
    
    print(f"\nTotal de eleitores que votaram: {voting_system.get_total_voters()}")

if __name__ == "__main__":
    main()

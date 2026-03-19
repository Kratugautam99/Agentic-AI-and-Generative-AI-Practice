import { runMemoryAgent, runAiSupportAgent } from './agents';

async function main() {
  const query = 'what are 3 most important statistical concepts?';

  // First, run the memory agent to retrieve relevant chunks
  const chunks = await runMemoryAgent(query);

  // Then, run the AI support agent with the query and retrieved chunks
  const completion = await runAiSupportAgent({
    chunks,
    query,
  });

  console.log('Completion:', completion);
}

main();
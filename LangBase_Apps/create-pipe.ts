import 'dotenv/config';
import { Langbase } from 'langbase';

const langbase = new Langbase({
  apiKey: process.env.LANGBASE_API_KEY!,
});

// Define the support AI agent pipe by giving name, description, and a system prompt.
async function main() {
  const supportAgent = await langbase.pipes.create({
    name: 'ai-maths-agent',
    description: 'An AI agent to support users with their maths queries.',
    messages: [
      {
        role: 'system',
        content: 'You\'re a helpful AI assistant. You will assist users with their maths queries.',
      },
    ],
  });

  console.log('Support agent:', supportAgent);
}
main();
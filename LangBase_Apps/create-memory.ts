import 'dotenv/config';
import { Langbase } from 'langbase';

const langbase = new Langbase({
  apiKey: process.env.LANGBASE_API_KEY!,
});

async function main() {
  const memory = await langbase.memories.create({
    name: 'stats-text-book',
    description: 'An AI memory for agentic memory course',
    embedding_model: 'google:text-embedding-004',
  });

  console.log('AI Memory:', memory);
}

main();
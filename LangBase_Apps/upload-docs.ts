import 'dotenv/config';
import { Langbase } from 'langbase';
import { readFile } from 'fs/promises';
import path from 'path';

const langbase = new Langbase({
  apiKey: process.env.LANGBASE_API_KEY!,
});

async function main() {
  const cwd = process.cwd();
  const memoryName = 'stats-text-book';

  // Read the statistical concepts file
  const statsConcepts = await readFile(path.join(cwd, 'docs', 'statistical-concepts.txt'));

  // Upload the doc to Langbase memory
  const statsResult = await langbase.memories.documents.upload({
    memoryName,
    contentType: 'text/plain',
    documentName: 'statistical-concepts.txt',
    document: statsConcepts,
    meta: { category: 'Education', topic: 'Statistics Concepts' },
  });

  console.log(statsResult.ok ? '✓ Statistical concepts doc uploaded' : '✗ Statistical concepts doc failed');
}

main();
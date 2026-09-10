const workshop = {
    name: "Kamau Metalworks",
    town: "Gikomba, Nairobi",
    craftsman: "Joseph Kamau"
};

const jobs = [
    { type: "Sliding gate", material_kes: 18000, labour_kes: 8000, paid: true},
    { type: "Window grills", material_kes: 6500, labour_kes: 4500, paid: true},
    { type: "Door frames", material_kes: 4200, labour_kes: 2800, paid: false},
    { type: "Roof sheets", material_kes: 9800, labour_kes: 3200, paid: true},
    { type: "Security door", material_kes: 12000, labour_kes: 7000, paid: false}
]

const totalRevenue = jobs
    .filter(j => j.paid)
    .reduce((sum,j) => sum + j.material_kes + j.labour_kes, 0);

const unpaidcount = jobs.filter(j => !j.paid).length;

console.log(`Workshop: ${workshop.name} | ${workshop.town}`);
console.log(`Craftsman: ${workshop.craftsman}`);
console.log(`Jobs completed: ${jobs.length}`);
console.log(`Revenue collected: KES ${totalRevenue.toLocaleString()}`);
console.log(`Unpaid jobs: ${unpaidcount}`);
console.log("\nJob brakdown:");
for (const job of jobs) {
    const total = job.material_kes + job.labour_kes;
    const status = job.paid ? "PAID" : "UNPAID";
    console.log(` ${job.type} | KES ${total.toLocaleString()} | ${status}`)
}